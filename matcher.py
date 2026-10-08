import json


def load_skills():

    with open("skills.json", "r") as file:
        data = json.load(file)

    skills = []

    for category in data:
        skills.extend(data[category])

    return skills


def extract_skills(text):

    text = text.lower()

    skills = load_skills()

    found_skills = []

    for skill in skills:

        if skill.lower() in text:
            found_skills.append(skill)

    return list(set(found_skills))
def match_resume(resume_text, job_description):

    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    matched = []

    for skill in job_skills:

        if skill in resume_skills:
            matched.append(skill)

    missing = []

    for skill in job_skills:

        if skill not in resume_skills:
            missing.append(skill)

    if len(job_skills) > 0:
        score = (len(matched) / len(job_skills)) * 100
    else:
        score = 0

    return {
        "score": round(score, 2),
        "matched": matched,
        "missing": missing
    }