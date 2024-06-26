from fpdf import FPDF

# Create PDF
pdf = FPDF(
    orientation='P', # 'L'
    unit='pt', # Units of the Fonts
    format='A4',
)

# Add Page
pdf.add_page()

# Image
pdf.image('Automations/PDFs/PDF Creator/UEM - cópia.png',
          w=80, h=80)

# Title
pdf.set_font(family='Times', style='B', size=24)
pdf.cell(w=0, h=50, txt='UEM University',
         align='C', ln=1)

# Body
pdf.set_font(family='Times', style='B', size=16)
pdf.cell(w=0, h=30, txt='Description', ln=1)

pdf.set_font(family='Times', size=11)
txt1 = """
   Universidade Estadual de Maringá (UEM), localizada em Maringá, Paraná, Brasil, é uma das instituições de ensino superior mais reconhecidas do país. Fundada em 1970, a UEM oferece uma ampla gama de cursos de graduação e pós-graduação, abrangendo diversas áreas do conhecimento, como ciências humanas, exatas, biológicas e agrárias. Com uma infraestrutura moderna, a universidade conta com laboratórios bem equipados, bibliotecas, centros de pesquisa e um hospital universitário. Além disso, a UEM é conhecida por sua forte ênfase em pesquisa e extensão, contribuindo significativamente para o desenvolvimento científico e tecnológico da região.
   A UEM também se destaca por sua comunidade acadêmica vibrante e diversificada, composta por estudantes, professores e pesquisadores de várias partes do Brasil e do mundo. A universidade promove a inclusão social e oferece diversos programas de apoio estudantil, como bolsas de estudo, assistência social e oportunidades de intercâmbio internacional. A vida no campus é enriquecida por atividades culturais, esportivas e sociais, criando um ambiente propício para o desenvolvimento pessoal e acadêmico dos estudantes. Com um compromisso contínuo com a excelência e a inovação, a UEM se mantém como uma instituição de referência no cenário educacional brasileiro."""
pdf.multi_cell(w=0, h=20, txt=txt1)
pdf.cell(w=0, h=20, txt='', ln=2)

pdf.set_font(family='Times', size=11)
pdf.cell(w=60, h=30, txt='Writen By:')
pdf.set_font(family='Times', style='B', size=11)
pdf.cell(w=50, h=30, txt='Gustavo Meira', ln=1)

pdf.output('Automations/PDFs/PDF Creator/output.pdf')