# Import libraries
import pandas as pd
import numpy as np
import random

# Set random seed for reproducibility
np.random.seed(42)
random.seed(42)

# Define number of leads
n_leads = 10000

# Define value pools for categorical fields
car_makes = ["Toyota", "Ford", "Honda", "Chevrolet", "Nissan", "BMW", "Mercedes", "Hyundai", "Kia", "Volkswagen"]
car_models = ["Corolla", "F-150", "Civic", "Silverado", "Altima", "3 Series", "C-Class", "Elantra", "Sorento", "Jetta"]
ownership_types = ["Owned", "Financed", "Leased"]
marital_statuses = ["Single", "Married", "Divorced", "Widowed"]
education_levels = ["High School", "Some College", "Associate Degree", "Bachelor's Degree", "Master's Degree", "Doctorate"]
homeowner_statuses = ["Homeowner", "Renter", "Living with Family"]
employment_statuses = ["Employed Full-Time", "Employed Part-Time", "Self-Employed", "Unemployed", "Retired"]
genders = ["Male", "Female", "Other"]
contact_methods = ["Phone", "Email", "Text", "Mail"]
lead_sources = ["Website", "Referral", "Event", "Cold Call", "Email Campaign"]
device_types = ["Desktop", "Mobile", "Tablet"]
insurance_statuses = ["Yes", "No"]
yes_no = ["Yes", "No"]
regions = ["Northeast", "Midwest", "South", "West"]
outdoor_activity_levels = ["Low", "Medium", "High"]
purchase_intentions = ["High", "Medium", "Low"]
vehicle_uses = ["Personal", "Business", "Mixed"]
language_preferences = ["English", "Spanish", "Other"]
military_statuses = ["Veteran", "Active Duty", "None"]

# Helper functions to generate fields
def generate_age():
    return np.random.choice(range(18, 90), p=np.linspace(1, 3, 72) / np.sum(np.linspace(1, 3, 72)))

def generate_income():
    return np.random.choice(["<30K", "30-50K", "50-75K", "75-100K", "100-150K", "150K+"],
                            p=[0.15, 0.2, 0.25, 0.2, 0.15, 0.05])

def generate_credit_score():
    return np.random.choice(["<600", "600-649", "650-699", "700-749", "750-800", "800+"],
                            p=[0.1, 0.2, 0.3, 0.25, 0.1, 0.05])

def generate_vehicle_year():
    return random.randint(2005, 2023)

def generate_mileage():
    return random.randint(0, 200000)

def generate_lead_score(age, income, credit, vehicle_year):
    base_score = 0
    income_tiers = {"<30K": -10, "30-50K": -5, "50-75K": 0, "75-100K": 5, "100-150K": 10, "150K+": 15}
    credit_tiers = {"<600": -10, "600-649": -5, "650-699": 0, "700-749": 5, "750-800": 10, "800+": 15}
    base_score += income_tiers[income]
    base_score += credit_tiers[credit]

    # Age influence
    if age < 30:
        base_score -= 10
    elif 55 <= age < 75:
        base_score += 10
    elif age >= 75:
        base_score += 20

    # Vehicle year influence
    if vehicle_year >= 2018:
        base_score += 5
    elif vehicle_year <= 2010:
        base_score -= 5

    base_score += np.random.normal(0, 10)  # random noise
    return int(np.clip(base_score + 50, 0, 100))

def generate_purchased(lead_score):
    return np.random.choice([1, 0], p=[min(lead_score/150, 0.85), 1 - min(lead_score/150, 0.85)])

# Create the main dataset
data = []
for _ in range(n_leads):
    age = generate_age()
    income = generate_income()
    credit = generate_credit_score()
    vehicle_year = generate_vehicle_year()
    mileage = generate_mileage()
    lead_score = generate_lead_score(age, income, credit, vehicle_year)
    purchased = generate_purchased(lead_score)

    record = {
        "Age": int(age),
        "Household_Income": income,
        "Credit_Score_Range": credit,
        "Vehicle_Year": vehicle_year,
        "Current_Mileage": mileage,
        "Lead_Score": lead_score,
        "Purchased": purchased,
        "Car_Make": random.choice(car_makes),
        "Car_Model": random.choice(car_models),
        "Ownership_Type": random.choice(ownership_types),
        "Marital_Status": random.choice(marital_statuses),
        "Education_Level": random.choice(education_levels),
        "Homeowner_Status": random.choice(homeowner_statuses),
        "Employment_Status": random.choice(employment_statuses),
        "Gender": random.choice(genders),
        "Preferred_Contact_Method": random.choice(contact_methods),
        "Lead_Source": random.choice(lead_sources),
        "Device_Type": random.choice(device_types),
        "Insurance_Status": random.choice(insurance_statuses),
        "Do_Not_Call": random.choice(yes_no),
        "Email_Opt_In": random.choice(yes_no),
        "Visited_Website_Last_30_Days": random.choice(yes_no),
        "Clicked_Email_Last_30_Days": random.choice(yes_no),
        "Opened_Email_Last_30_Days": random.choice(yes_no),
        "Region": random.choice(regions),
        "Zip_Code": random.randint(10000, 99999),
        "Phone_Valid": random.choice(yes_no),
        "Email_Valid": random.choice(yes_no),
        "Vehicle_Use": random.choice(vehicle_uses),
        "Language_Preference": random.choice(language_preferences),
        "Military_Status": random.choice(military_statuses),
        "Has_Children": random.choice(yes_no),
        "Outdoor_Activity_Level": random.choice(outdoor_activity_levels),
        "Purchase_Intention": random.choice(purchase_intentions),
        "Number_of_Vehicles": random.randint(1, 5),
        "Years_in_Current_Home": random.randint(0, 40),
        "Past_Warranty_Purchase": random.choice(yes_no),
        "Service_History": random.choice(["Regular", "Occasional", "None"]),
        "Recent_Move": random.choice(yes_no),
        "Household_Size": random.randint(1, 6),
        "Estimated_Home_Value": random.choice(["<100K", "100-200K", "200-400K", "400-600K", "600K+"]),
        "Estimated_Rent": random.choice(["<500", "500-1000", "1000-1500", "1500-2000", "2000+"]),
        "Utilities_Included": random.choice(yes_no),
        "Subscribed_To_Competitor": random.choice(yes_no),
        "Warranty_Interest_Level": random.choice(["High", "Medium", "Low"]),
        "Credit_Card_Holder": random.choice(yes_no),
        "Bank_Loan": random.choice(yes_no),
        "Social_Media_Engagement": random.choice(["High", "Medium", "Low"]),
        "Online_Shopping_Frequency": random.choice(["High", "Medium", "Low"]),
        "Mobile_App_User": random.choice(yes_no),
        "Streaming_Services_User": random.choice(yes_no),
        "Data_Sharing_Consent": random.choice(yes_no),
    }
    data.append(record)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("synthetic_leads_dataset.csv", index=False)

print("✅ Dataset created and saved as 'synthetic_leads_dataset.csv'!")

