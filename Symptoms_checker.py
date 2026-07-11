diseases = {
    "Flu": {
        "symptoms": ["fever", "cough", "fatigue", "body aches", "headache", "chills", "sore throat", "runny nose"],
        "advice": "Rest, stay hydrated, and consider antiviral medication if caught early."
    },
    "Common Cold": {
        "symptoms": ["runny nose", "sneezing", "sore throat", "cough", "mild fever", "congestion", "fatigue"],
        "advice": "Rest and fluids. Symptoms usually resolve in 7-10 days."
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "fatigue", "loss of taste", "loss of smell", "shortness of breath", "body aches", "headache", "chills"],
        "advice": "Isolate, seek testing, and consult a doctor if symptoms worsen."
    },
    "Pneumonia": {
        "symptoms": ["fever", "cough", "shortness of breath", "chest pain", "fatigue", "chills", "sweating"],
        "advice": "Seek medical attention promptly. May require antibiotics or hospital care."
    },
    "Gastroenteritis": {
        "symptoms": ["nausea", "vomiting", "diarrhea", "stomach pain", "fever", "fatigue", "loss of appetite"],
        "advice": "Stay hydrated. Use oral rehydration salts. Seek help if symptoms persist."
    },
    "Malaria": {
        "symptoms": ["fever", "chills", "sweating", "headache", "nausea", "fatigue", "vomiting", "body aches"],
        "advice": "Requires prompt medical diagnosis and antimalarial treatment."
    },
    "Dengue Fever": {
        "symptoms": ["high fever", "severe headache", "joint pain", "body aches", "rash", "nausea", "fatigue", "vomiting"],
        "advice": "No specific treatment; rest, fluids, and pain relief. Avoid aspirin."
    },
    "Typhoid": {
        "symptoms": ["high fever", "headache", "stomach pain", "constipation", "weakness", "loss of appetite", "rash"],
        "advice": "Requires antibiotics prescribed by a doctor. Stay hydrated."
    },
    "Migraine": {
        "symptoms": ["severe headache", "nausea", "vomiting", "sensitivity to light", "sensitivity to sound", "dizziness"],
        "advice": "Rest in a dark quiet room. Pain relievers may help. Consult a neurologist if frequent."
    },
    "Asthma": {
        "symptoms": ["shortness of breath", "wheezing", "cough", "chest tightness", "fatigue"],
        "advice": "Use prescribed inhaler. Avoid triggers. Seek emergency care if severe."
    },
    "Anemia": {
        "symptoms": ["fatigue", "weakness", "pale skin", "shortness of breath", "dizziness", "cold hands", "headache"],
        "advice": "Iron-rich diet or supplements. Treat underlying cause with a doctor's guidance."
    }
}


def get_confidence_label(matched, total):
    percentage = (matched / total) * 100
    if percentage >= 50:
        return "High"
    elif percentage >= 25:
        return "Medium"
    else:
        return "Low"


def check_symptoms(user_symptoms):
    results = []

    for disease, data in diseases.items():
        matched_symptoms = []

        for symptom in user_symptoms:
            if symptom in data["symptoms"]:
                matched_symptoms.append(symptom)

        if len(matched_symptoms) > 0:
            confidence = get_confidence_label(len(matched_symptoms), len(data["symptoms"]))
            results.append({
                "disease": disease,
                "matched": matched_symptoms,
                "matched_count": len(matched_symptoms),
                "total": len(data["symptoms"]),
                "confidence": confidence,
                "advice": data["advice"]
            })

    results.sort(key=lambda x: x["matched_count"], reverse=True)
    return results


def display_results(results):
    if len(results) == 0:
        print("\nNo matching diseases found. Try entering more symptoms.")
        return

    print("\n" + "=" * 55)
    print("  POSSIBLE CONDITIONS")
    print("=" * 55)

    for i, result in enumerate(results):
        print(f"\n  {i + 1}. {result['disease']}")
        print(f"     Match      : {result['confidence']}")
        print(f"     Symptoms   : {result['matched_count']} of {result['total']} matched")
        print(f"     Matched    : {', '.join(result['matched'])}")
        print(f"     Advice     : {result['advice']}")

    print("\n" + "-" * 55)
    print("  NOTE: This is not a medical diagnosis.")
    print("  Please consult a qualified healthcare professional.")
    print("-" * 55)


def get_user_symptoms():
    user_symptoms = []

    print("\nEnter your symptoms one by one.")
    print("Type 'done' when finished.\n")

    while True:
        symptom = input("  Symptom: ").strip().lower()

        if symptom == "done":
            break
        elif symptom == "":
            print("  Please enter a symptom or type 'done' to finish.")
        elif symptom in user_symptoms:
            print(f"  '{symptom}' already added.")
        else:
            user_symptoms.append(symptom)
            print(f"  Added: {symptom}")

    return user_symptoms


def main():
    print("=" * 55)
    print("       DISEASE SYMPTOM CHECKER")
    print("=" * 55)
    print("  A basic healthcare decision assistant.")

    while True:
        user_symptoms = get_user_symptoms()

        if len(user_symptoms) == 0:
            print("\n  No symptoms entered. Please try again.")
        else:
            print(f"\n  Checking {len(user_symptoms)} symptom(s): {', '.join(user_symptoms)}")
            results = check_symptoms(user_symptoms)
            display_results(results)

        print("\nWould you like to check another set of symptoms?")
        again = input("  Enter 'yes' to continue or anything else to exit: ").strip().lower()

        if again != "yes":
            print("\n  Thank you for using the Disease Symptom Checker.")
            print("  Stay healthy!\n")
            break


main()
