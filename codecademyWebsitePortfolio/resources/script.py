
new_text = []
resume_list = []

class Employer:
    def __init__(self, name):
        self.name = name
        self.info_dict = {
            'NAME' : self.name,
            'LOCATION': [],
            'TITLES': []
        }

class Employer_Title:
    def __init__(self, title):
        self.title_name = title
        self.date = ''
        self.list = []

class Eduction:
    def __init__(self, name):
        self.name = name
        self.info_dict = {
            'NAME': self.name,
            'DATE' : [],
            'LOCATION' : [],
            'LI' : []
        }

class Skills:
    def __init__(self):
        self.name = "Skills"
        self.info_dict = {
            'NAME': 'SKILLS',
            'LI' : []
        }

with open("./resources/resume_no_format.txt") as file1:
    lines = file1.readlines()
    for line in lines:
        line = line.strip()
        if line != '':
            new_text.append(line)
    current_focus = ''
    secondary_focus = ''
    for item in new_text:
        item_list = item.split('!')
        desc = item_list[0]
        info = item_list[1]
        if item_list[0] == 'EMPLOYER':
            employer = Employer(item_list[1])
            resume_list.append(employer)
            current_focus = employer
            secondary_focus = ''
        elif item_list[0] == 'TITLE':
            new_title = Employer_Title(info)
            secondary_focus = new_title
            current_focus.info_dict['TITLES'].append(new_title)
        elif item_list[0] == 'EDUCATION':
            education = Eduction(item_list[1])
            resume_list.append(education)
            current_focus = education
            secondary_focus = ''
        elif item_list[0] == 'SKILLS':
            skills = Skills()
            resume_list.append(skills)
            current_focus = skills
            secondary_focus = ''
        elif secondary_focus != '':
            if desc == 'LI':
                secondary_focus.list.append(info)
            else:
                secondary_focus.date = info
        else:
            current_focus.info_dict[item_list[0]].append(item_list[1])
    file1.close()

file2 = open("./resources/exp_report.html", "w")
file2.write("<html>\n\t<head>\n\t\t<title>Resume Report</title>")
file2.write("\n\t\t<link href=\"resume.css\" rel=\"stylesheet\">\n\t</head>")
file2.write("\n\t<body>\n\t\t<header>\n\t\t<h1>Resume</h1>\n\t</header>\n\t<main>")
file2.write("\n\t\t<section id=\"employers\">\n\t\t\t<h2>Professional Experience</h2>")
for item in resume_list:
    if type(item) == Employer:
        file2.write(f"\n\t\t\t<div id=\"{item.name}\">")
        for key, value in item.info_dict.items():
            if key == 'NAME':
                file2.write(f"\n\t\t\t\t<h3>{value}</h3>")
            elif key == 'LOCATION':
                for location in value:
                    file2.write(f"\n\t\t\t\t\t<p>Location: {location}</p>")
            elif key == 'TITLES':
                file2.write("\n\t\t\t\t<h4>Positions Held:</h4>")
                for title in value:
                    file2.write(f"\n\t\t\t\t<h5>{title.title_name}</h5>")
                    file2.write(f"\n\t\t\t\t\t<p>{title.date}</p>\n\t\t\t\t\t<ul>")
                    for li in title.list:
                        file2.write(f"\n\t\t\t\t\t\t<li>{li}</li>")
                    file2.write(f"\n\t\t\t\t\t</ul>")
        file2.write("\n\t\t\t</div>")
file2.write("\n\t\t\t</section>")
file2.write("\n\t\t\t<section id=\"education\">")
file2.write("\n\t\t\t\t<h2>Education:</h2>")
for item in resume_list:
    if type(item) == Eduction:
        file2.write(f"\n\t\t\t<div id=\"{item.info_dict['NAME']}\">")
        for key, values in item.info_dict.items():
            if key == 'NAME':
                file2.write(f"\n\t\t\t\t<h3>{values}</h3>")
            elif key == "LOCATION":
                file2.write(f"\n\t\t\t\t<h4>Location(s):</h4>")
                for i in values:
                    file2.write(f"\n\t\t\t\t\t<p>{i}</p>")
            elif key == "DATE":
                file2.write(f"\n\t\t\t\t\t<p>Dates</p>")
                for i in values:
                    file2.write(f"\n\t\t\t\t\t<p>{i}</p>")
            else:
                file2.write(f"\n\t\t\t\t<h5>Notes</h5>\n\t\t\t\t<ul>")
                for li in values:
                    file2.write(f"\n\t\t\t\t\t<li>{li}</li>")
                file2.write("\t\t\t\t</ul>")
        file2.write("\n\t\t\t</div>")
file2.write("\n\t\t</section>")
file2.write("\n\t\t<section id=\"skills\">")
file2.write("\n\t\t\t<h2>Skills:</h2>\n\t\t\t\t<ul>")
for item in resume_list:
    if type(item) == Skills:
        for i in item.info_dict['LI']:
            file2.write(f"\n\t\t\t\t\t<li>{i}</li>")
file2.write("\n\t\t\t</section>")
file2.write("\n\t\t</main>\n\t</body>\n</html>")
file2.close()