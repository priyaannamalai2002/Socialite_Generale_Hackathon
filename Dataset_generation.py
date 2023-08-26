import random
import pandas as pd

job_skills = [
    ("Software Engineer", ["Programming (e.g., Python, Java, C++)", "Problem-solving", "Algorithms"]),
    ("Data Scientist", ["Data analysis", "Machine learning", "Statistics"]),
    ("Web Developer", ["HTML", "CSS", "JavaScript", "Front-end frameworks (e.g., React)"]),
    ("Technical Project Manager", ["Project planning", "Resource management", "Agile methodologies"]),
    ("HR Business Partner", ["HR Generalist Activities", "HRBP", "HR Business Partner"]),
    ("IT Support Analyst", ["Excellent Communication Skills", "Willingness to Learn", "Positive Attitude", "Management", "SQL", "UNIX", "Production Support", "Monitoring", "Night Shifts"]),
    ("Application Support Manager", ["Application Support Delivery Manager"]),
    ("IT Security Auditor", ["Cyber Security", "IT Risk", "IT Audit", "Information Security Audit", "CISA", "ITGC", "System Audit"]),
    ("Quality Assurance Specialist", ["Quality Assurance", "QMS", "Auditing", "Quality Engineering", "Marketing", "Process Audit", "ISO 9001", "Product Quality"]),
    ("Sales Representative", ["Selling Skills", "Mass Mailing", "Sales", "Direct Marketing", "Life Insurance"]),
    ("Java Developer", ["Good Communication Skills", "Implementation", "Support", "Experience", "Projects", "Java", "PL/SQL", "Consultant"]),
    ("UI/UX Developer", ["JSON", "Java", "J2EE", "JavaScript", "XML", "HTML", "JSP", "Application Development", "User Interface", "UI Design"]),
    ("Sales Manager", ["Sales", "Business Development", "Products", "Sales Manager"]),
    ("Web Developer", ["AngularJS", "Ruby on Rails", "Ruby", "Rails"]),
    ("Software Engineer", ["ICC", "Innovus", "P&R", "Timing Closure", "SoC Encounter", "IR Drop", "RTL Compiler", "Prime Time", "Physical Design"]),
    ("Recruitment Specialist", ["US IT Staffing", "US Recruitment", "US IT Recruitment"]),
    ("Customer Care Executive", ["Inbound", "Outbound", "Voice Process", "Hiring", "Interviewing", "Communication Skills", "Customer Care", "BPO", "CSE"]),
    ("IT Deployment Specialist", ["Configuration", "Google Application Deployment", "Office 365 Migration", "Networking", "Linux Administration", "Cloud"]),
    ("Finance Analyst", ["Finance and Tax"]),
    ("Oracle Database Administrator", ["Technical Specifications", "MySQL Server", "Oracle Database 9i", "Oracle Development", "Software Development"]),
    ("Digital Marketing Specialist", ["Web Technologies", "Data Strategy", "Web Analytics", "CRM", "Targeting", "Marketing Strategy"]),
    ("System Administrator", ["NAGIOS", "SSH", "Hadoop", "AWS", "Apache", "Ubuntu", "Linux Administration", "MySQL", "Redhat"]),
    ("Electrical Technician", ["ITI", "Diploma", "Fitter", "Industrial Training Institute", "ITI Electrical", "ITI Fitter", "Electrician"]),
    ("Regional Sales Manager", ["Regional Sales", "Marketing Support", "Brand Building", "PR", "Events", "CRM", "Strategy", "Agency Management"]),
    ("Company Secretary", ["Company Secretary"]),
    ("Business Growth Manager", ["Region", "Business Growth", "Sales Management", "Marketing Operations", "Business Development", "Key Account Management"]),
    ("Gas Turbine Engineer", ["Gas Turbine", "Manufacturing Engineering"]),
    ("Assistant Manager", ["Assistant Manager PED", "AM PED", "Team Leader PED", "Senior Executive PED", "Team Manager PED"]),
    ("Taxation Specialist", ["International Taxation", "Indian GAAP", "Transfer Pricing Manager", "Accounting Standards", "Chartered Accountant"]),
    ("IT Analyst", ["FX", "Forex", "Treasury"]),
    ("PPC Executive", ["PPC Executive", "Production Planning Control Executive"]),
    ("Front Office Coordinator", ["Front Office Executive", "Front Desk Executive", "FOE", "Guest Relation Executive", "Receptionist"]),
    ("Grass GIS Specialist", ["GRASS GIS"]),
    ("US Staffing Specialist", ["US Staffing", "Client Acquisition"]),
    ("Customer Support", ["Customer Support", "Customer Executive", "Customer Care"]),
    ("VP of Engineering", ["VP Engineering", "Algorithm", "Data Structures", "Technical Solutions"]),
    ("Tele-Marketer", ["Tele-Marketing", "Call Center", "Tele-Sales", "Telemarketing"]),
    ("Java Developer", ["Java", "J2EE", "HTML", "JSP", "EJB", "Coding", "ATG", "Content Management", "Travel", "Merchandising"]),
    ("Primary School Teacher", ["Primary Teacher", "Teaching", "Mathematics", "Science"]),
    ("Medical Coder", ["Medical Coding Jobs", "Medical Coder", "Nursing Jobs", "Pharma Jobs", "Biotechnology Jobs", "Biochemistry Jobs"]),
    ("Training Coordinator", ["Training Management", "Publicity", "CSR", "Recruitment", "Policies"]),
    ("Pharmaceuticals Expert", ["Tablets", "Team Handling", "NDDS", "Capsule", "Pellets", "Solid Oral Dosage"]),
    ("OpenText Specialist", ["OpenText", "Invoice Management", "SAP Workflow", "Purchase Orders", "SAP_ALV", "Media Management", "DAM", "Digital Media"]),
    ("Finance Application Designer", ["Data Design", "Data Governance", "Finance Module", "Financial Implementation", "Banking Application"]),
    ("IT Support Specialist", ["MSBuild", "JSON", "ASP.Net", "WCF", "MS SQL Server", "C#", "Classic ASP", "Javascript", "JQuery", "IIS"]),
    ("X-Ray Technician", ["USG", "X-Ray", "Ultrasound", "CT", "MRI", "Typist"]),
    ("Bloomberg Terminal Specialist", ["Bloomberg Terminal"]),
    ("Network Administrator", ["Configuration", "L2", "UNIX", "Solaris", "SAN", "Troubleshooting", "DNS", "WAN", "NAS", "DHCP"]),
    ("Pre Acquisition Analyst", ["Pre Acquisition", "Risk", "Credit Underwriting", "Credit Policies", "Credit Risk"]),
]

num_samples = 400  # Specify the number of samples or instances in the dataset

# Generate random data for each field
data = []
for _ in range(num_samples):
    job_title, skills_needed = random.choice(job_skills)
    skill_set = random.sample(skills_needed, random.randint(1, len(skills_needed)))
    data.append([job_title, skill_set])

# Create a pandas DataFrame with the generated data
df = pd.DataFrame(data, columns=["Job Role Title", "Job Description", "Skill Set Needed"])

# Save the DataFrame as a CSV file
df.to_csv("generated_dataset.csv")
