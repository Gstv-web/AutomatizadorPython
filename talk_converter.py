from ura_report_converter import URAReportConverterInterface
from ura_report import URAReport
from xml.dom import minidom


class TalkConverter(URAReportConverterInterface):

    def convert_ura_report(self, report: URAReport):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.call_interaction_file)
        self.writer.set_activation_styles()
        self.writer.insert_interaction_headers()
        self.writer.set_call_interaction_styles()
        # self.writer.remove_blacklist_numbers()
        self.writer.save()


    def cast_activation_report(self, activation_file_name):
        with open(activation_file_name, 'r', encoding='utf-8') as f:
            xml = minidom.parse(f)
            col_num = xml.getElementsByTagName("Numero")
            col_date = xml.getElementsByTagName("DataHora")
            col_duratuion = xml.getElementsByTagName("Duração")
            col_status = xml.getElementsByTagName("Status")

            num = []
            date = []
            duration = []
            status = []

            for n in col_num:
                num.append(n.firstChild.data)
            
            for d in col_date:
                pre_date = d.firstChild.data.split("T")
                if "-" in pre_date[0]:
                    edit = pre_date[0].split("-")
                    if len(edit[0]) == 4:
                        edit.reverse()
                        bar = "/".join(edit)
                        new_date = bar
                        date.append(new_date)
            
            for d in col_duratuion:
                duration.append(d.firstChild.data)

            for s in col_status:
                status.append(s.firstChild.data)

            atendida = []
            nao_atendida = []
            ocupada = []
            servico = []
            congestionamento = []

            for n, d, dr, s in zip(num, date, duration, status):
                if s == "Atendida":
                    atendida.append([n, d, dr, s])

            for n, d, dr, s in zip(num, date, duration, status):
                if s == "Não Atendida":
                    nao_atendida.append([n, d, dr, s])

            for n, d, dr, s in zip(num, date, duration, status):
                if s == "Ocupada":
                    ocupada.append([n, d, dr, s])

            for n, d, dr, s in zip(num, date, duration, status):
                if s == "Serviço":
                    servico.append([n, d, dr, s])

            for n, d, dr, s in zip(num, date, duration, status):
                if s == "Congestionamento":
                    congestionamento.append([n, d, dr, s])
    
            for i in range(len(atendida)):
                self.writer.write_activation_message(atendida[i])

            for i in range(len(nao_atendida)):
                self.writer.write_activation_message(nao_atendida[i])

            for i in range(len(ocupada)):
                self.writer.write_activation_message(ocupada[i])

            for i in range(len(servico)):
                self.writer.write_activation_message(servico[i])

            for i in range(len(congestionamento)):
                self.writer.write_activation_message(congestionamento[i])

    def cast_call_interaction_report(self, call_interaction_file_name):
        with open(call_interaction_file_name, 'r', encoding='utf-8') as f:
            xml = minidom.parse(f)
            col_num = xml.getElementsByTagName("Numero")
            col_date = xml.getElementsByTagName("DataHora")
            col_interaction = xml.getElementsByTagName("Digito")

            num = []
            date = []
            interaction =[]

            for n in col_num:
                num.append(n.firstChild.data)
            
            for d in col_date:
                pre_date = d.firstChild.data.split("T")
                if "-" in pre_date[0]:
                    edit = pre_date[0].split("-")
                    if len(edit[0]) == 4:
                        edit.reverse()
                        bar = "/".join(edit)
                        new_date = bar
                        date.append(new_date)

            for tag in col_interaction:
                if tag.firstChild == None:
                    new_tag = ""
                    interaction.append(new_tag)
                elif "-" in tag.firstChild.data:
                    new_tag = tag.firstChild.data.replace("-", "")
                    if len(new_tag) > 1:
                        interaction.append(list(new_tag))

            

            for p, d, i in zip(num, date, interaction):
                self.writer.write_call_interaction_message([p, d, *i])
              