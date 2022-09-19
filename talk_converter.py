from ura_report_converter import URAReportConverterInterface
from ura_report import URAReport
from xml.dom import minidom


class TalkConverter(URAReportConverterInterface):

    def convert_ura_report(self, report: URAReport):
        self.cast_activation_report(report.activation_file)
        self.cast_call_interaction_report(report.call_interaction_file)
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

            for n, d, dr, s in zip(num, date, duration, status):
                self.writer.write_activation_message([n, d, dr, s])


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
                else:
                    interaction.append(str(tag.firstChild.data))

            for i, data in enumerate(interaction):
                # digito[i].replace("-", "")
                if "-" in interaction[i]:
                    new_digito = interaction[i].replace("-", "").replace(" ","")
                    interaction[i] = list(new_digito)

            
            final = []
            interaction_split = []

            for data in interaction:
                length = len(data)
                max_length = 0
                if length > max_length:
                    max_length = length
            

            for p, d, i in zip(num, date, interaction):
                final.append([p, d, i])
              

            for i in range(len(final)):
                self.writer.write_call_interaction_message(str(final[i]))