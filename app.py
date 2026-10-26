
import streamlit as st
from datetime import date
from bson import ObjectId
from db import db

st.set_page_config(
    page_title="MediCare+ | Hospital Management System",
    page_icon="🏥",
    layout="wide"
)



st.markdown("""
<style>
.stApp {
    background: #F4F9F4;
    color: #20352A;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1440px;
    padding: 2rem 2rem 3rem;
}

/* Forest-green sidebar */
[data-testid="stSidebar"] {
    background: #164E35;
}

[data-testid="stSidebar"] * {
    color: #F0F8F1;
}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
    font-size: 14px;
}

/* Headings */
h1, h2, h3 {
    color: #164E35 !important;
    font-weight: 700 !important;
}

/* White metric cards */
[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #DCEBDD;
    border-radius: 16px;
    padding: 20px;
    box-shadow: 0 4px 14px rgba(22, 78, 53, 0.05);
}

[data-testid="stMetricLabel"] {
    color: #607568;
}

[data-testid="stMetricValue"] {
    color: #164E35;
    font-weight: 750;
}

/* Forms and expanders */
[data-testid="stForm"],
[data-testid="stExpander"] {
    background: #FFFFFF;
    border: 1px solid #DCEBDD;
    border-radius: 14px;
}

/* Input fields */
[data-testid="stTextInput"] input,
[data-testid="stNumberInput"] input,
[data-testid="stDateInput"] input {
    border-radius: 9px;
    border-color: #C9DDCE;
}

/* Primary buttons */
.stButton > button[kind="primary"],
.stFormSubmitButton > button[kind="primary"] {
    background: #27845A;
    color: #FFFFFF;
    border: 1px solid #27845A;
    border-radius: 9px;
    font-weight: 600;
}

.stButton > button[kind="primary"]:hover,
.stFormSubmitButton > button[kind="primary"]:hover {
    background: #164E35;
    border-color: #164E35;
    color: #FFFFFF;
}

/* Other buttons */
.stButton > button,
.stFormSubmitButton > button {
    border-radius: 9px;
    min-height: 40px;
}

/* Tables */
[data-testid="stDataFrame"] {
    border: 1px solid #DCEBDD;
    border-radius: 12px;
}

/* Alerts */
[data-testid="stAlert"] {
    border-radius: 10px;
}

/* Responsive styling */
@media (max-width: 768px) {
    .block-container {
        padding: 1rem 0.75rem 2rem;
    }

    h1 {
        font-size: 1.7rem !important;
    }

    [data-testid="stMetric"] {
        padding: 12px;
        border-radius: 12px;
    }

    [data-testid="stMetricValue"] {
        font-size: 1.45rem;
    }

    .stButton > button,
    .stFormSubmitButton > button {
        width: 100%;
    }
}

@media (max-width: 480px) {
    .block-container {
        padding: 0.75rem 0.5rem 1.5rem;
    }

    h1 {
        font-size: 1.45rem !important;
    }
}

/* Fix dark input fields and invisible text */
.stApp,
[data-testid="stAppViewContainer"] {
    background-color: #F4F9F4 !important;
    color: #20352A !important;
}

/* Text inputs, number inputs and date inputs */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="input"] input,
.stApp [data-baseweb="textarea"] textarea {
    background-color: #FFFFFF !important;
    color: #20352A !important;
    -webkit-text-fill-color: #20352A !important;
    caret-color: #27845A !important;
    border-color: #C9DDCE !important;
}

/* Dropdown fields */
.stApp [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #20352A !important;
    border-color: #C9DDCE !important;
}

.stApp [data-baseweb="select"] input {
    background-color: transparent !important;
    color: #20352A !important;
    -webkit-text-fill-color: #20352A !important;
}

/* Input labels and placeholders */
.stApp [data-testid="stWidgetLabel"],
.stApp [data-testid="stWidgetLabel"] p,
.stApp label {
    color: #365443 !important;
}

.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #82958A !important;
    -webkit-text-fill-color: #82958A !important;
    opacity: 1 !important;
}

/* Number input controls */
.stApp [data-testid="stNumberInput"] button {
    background-color: #E4F1E7 !important;
    color: #164E35 !important;
    border-color: #C9DDCE !important;
}

/* Keep form cards white */
[data-testid="stForm"],
[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    color: #20352A !important;
    border-color: #DCEBDD !important;
}


/* ===== FINAL VISIBILITY FIX ===== */

/* All main-page text */
.stApp,
.stApp p,
.stApp label,
.stApp [data-testid="stMarkdownContainer"],
.stApp [data-testid="stWidgetLabel"],
.stApp [data-testid="stWidgetLabel"] p {
    color: #244735 !important;
}

/* Sidebar text stays readable on forest green */
[data-testid="stSidebar"],
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
[data-testid="stSidebar"] [data-testid="stWidgetLabel"],
[data-testid="stSidebar"] [data-testid="stWidgetLabel"] p {
    color: #FFFFFF !important;
}

/* Text inputs and number inputs */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="input"] input,
.stApp [data-baseweb="textarea"] textarea {
    background: #FFFFFF !important;
    color: #20352A !important;
    -webkit-text-fill-color: #20352A !important;
    caret-color: #27845A !important;
    border-color: #B8D6C1 !important;
}

/* Dropdowns */
.stApp [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #20352A !important;
}

.stApp [data-baseweb="select"] input {
    color: #20352A !important;
    -webkit-text-fill-color: #20352A !important;
}

/* All regular buttons */
.stApp button,
.stApp button p,
.stApp button span {
    color: #164E35 !important;
}

/* Primary and form-submit buttons */
.stApp button[kind="primary"],
.stApp button[kind="primary"] p,
.stApp button[kind="primary"] span,
.stApp [data-testid="stFormSubmitButton"] button,
.stApp [data-testid="stFormSubmitButton"] button p,
.stApp [data-testid="stFormSubmitButton"] button span {
    background-color: #27845A !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-color: #27845A !important;
}

/* Number input +/- buttons */
.stApp [data-testid="stNumberInput"] button {
    background-color: #E4F1E7 !important;
    color: #164E35 !important;
}

/* Keep forms clean and white */
[data-testid="stForm"],
[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    color: #244735 !important;
    border-color: #DCEBDD !important;
}

/* Placeholder visibility */
.stApp input::placeholder,
.stApp textarea::placeholder {
    color: #82958A !important;
    -webkit-text-fill-color: #82958A !important;
    opacity: 1 !important;
}

/* ===== FORCE LIGHT GREEN AND WHITE THEME ===== */

/* Main application */
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background-color: #F4F9F4 !important;
    color: #164E35 !important;
}

/* Entire sidebar white */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"] {
    background-color: #FFFFFF !important;
}

/* Sidebar text */
[data-testid="stSidebar"] *,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p {
    color: #164E35 !important;
}

/* Sidebar navigation dropdown */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    border: 1px solid #B8D6C1 !important;
}

/* All text inputs, number inputs and text areas */
.stApp input,
.stApp textarea,
.stApp [data-baseweb="input"],
.stApp [data-baseweb="textarea"] {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    -webkit-text-fill-color: #164E35 !important;
    caret-color: #27845A !important;
    border-color: #B8D6C1 !important;
}

/* All dropdowns: closed state */
.stApp [data-baseweb="select"] > div,
.stApp [data-baseweb="select"] input {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    -webkit-text-fill-color: #164E35 !important;
}

/* Dropdown option menu when opened */
[data-baseweb="popover"],
[data-baseweb="menu"],
[data-baseweb="menu"] ul,
[data-baseweb="popover"] ul {
    background-color: #FFFFFF !important;
}

[data-baseweb="menu"] li,
[data-baseweb="option"],
[role="option"] {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
}

/* Hovered dropdown option */
[data-baseweb="menu"] li:hover,
[data-baseweb="option"]:hover,
[role="option"]:hover {
    background-color: #E4F1E7 !important;
    color: #164E35 !important;
}

/* Radio buttons and checkboxes */
.stApp [data-testid="stCheckbox"],
.stApp [data-testid="stRadio"] {
    color: #164E35 !important;
}

/* Number +/- controls */
.stApp [data-testid="stNumberInput"] button {
    background-color: #E4F1E7 !important;
    color: #164E35 !important;
    border-color: #B8D6C1 !important;
}

/* Buttons: white background, green text */
.stApp button,
.stApp button p,
.stApp button span {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    -webkit-text-fill-color: #164E35 !important;
    border-color: #B8D6C1 !important;
}

/* Submit buttons: green background, white text */
.stApp [data-testid="stFormSubmitButton"] button,
.stApp [data-testid="stFormSubmitButton"] button p,
.stApp [data-testid="stFormSubmitButton"] button span {
    background-color: #27845A !important;
    color: #FFFFFF !important;
    -webkit-text-fill-color: #FFFFFF !important;
    border-color: #27845A !important;
}

/* Cards and forms */
[data-testid="stMetric"],
[data-testid="stForm"],
[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    border-color: #DCEBDD !important;
}

/* Headings */
.stApp h1,
.stApp h2,
.stApp h3 {
    color: #164E35 !important;
}


/* Restore original green sidebar */
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebarContent"] {
    background-color: #164E35 !important;
}

/* Sidebar text stays white */
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] {
    color: #FFFFFF !important;
}

/* Sidebar dropdown remains white */
[data-testid="stSidebar"] [data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    border-color: #B8D6C1 !important;
}

[data-testid="stSidebar"] [data-baseweb="select"] input {
    background-color: #FFFFFF !important;
    color: #164E35 !important;
    -webkit-text-fill-color: #164E35 !important;
}


/* MediCare+ sidebar branding */
.brand-container {
    text-align: center;
    padding: 22px 8px 24px;
    margin-bottom: 18px;
}

.brand-logo {
    width: 58px;
    height: 58px;
    line-height: 58px;
    margin: 0 auto 12px;
    border-radius: 18px;
    background: #FFFFFF;
    color: #27845A;
    font-size: 38px;
    font-weight: 800;
    box-shadow: 0 4px 15px rgba(0,0,0,0.10);
}

.brand-name {
    color: #FFFFFF;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -0.8px;
}


.brand-container {
    text-align: center;
    padding: 20px 5px 24px;
    margin-bottom: 18px;
    width: 100%;
}

.brand-logo {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 58px;
    height: 58px;
    margin: 0 auto 12px;
    border-radius: 18px;
    background: #FFFFFF;
    color: #27845A;
    font-size: 38px;
    font-weight: 800;
    box-shadow: 0 4px 15px rgba(0,0,0,0.12);
}

.brand-name {
    color: #FFFFFF !important;
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -0.8px;
    line-height: 1.4;
}

.brand-name span {
    color: #A7D7B5 !important;
}

.brand-tagline {
    color: #DCEFE1 !important;
    font-size: 9px;
    letter-spacing: 1.2px;
    line-height: 1.6;
    margin-top: 5px;
}

.brand-divider {
    height: 1px;
    background: rgba(255,255,255,0.22);
    margin-top: 22px;
}



</style>
""", unsafe_allow_html=True)


patients = db["patients"]
doctors = db["doctors"]
appointments = db["appointments"]

st.title("MediCare + ")
st.caption("Your hospital operations, all in one place.")
st.divider()


# MediCare+ Branding

st.sidebar.markdown("""
<div class="brand-container">
    <div class="brand-logo">✚</div>
    <div class="brand-name">MediCare<span>+</span></div>
    <div class="brand-tagline">HOSPITAL MANAGEMENT SYSTEM</div>
    <div class="brand-divider"></div>
</div>
""", unsafe_allow_html=True)


menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Register Patient",
        "View Patients",
        "Manage Doctors",
        "Book Appointment",
        "View Appointments",
        "Reports & Analytics"
    ]
)


# DASHBOARD
if menu == "Dashboard":
    st.subheader("Hospital Statistics")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Patients", patients.count_documents({}))
    c2.metric("Total Doctors", doctors.count_documents({}))
    c3.metric("Total Appointments", appointments.count_documents({}))

    st.info("Welcome to the Hospital Management System.")

# REGISTER PATIENT
elif menu == "Register Patient":
    st.subheader("Register New Patient")

    with st.form("patient_form"):
        name = st.text_input("Patient Name")
        age = st.number_input("Age", min_value=0, max_value=120, step=1)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        phone = st.text_input("Phone Number")
        department = st.selectbox(
            "Department",
            ["General Medicine", "Cardiology", "Orthopedics",
             "Neurology", "Pediatrics"]
        )

        submitted = st.form_submit_button("Register Patient")

        if submitted:
            if not name.strip() or not phone.strip():
                st.error("Please enter patient name and phone number.")
            else:
                patients.insert_one({
                    "name": name.strip(),
                    "age": age,
                    "gender": gender,
                    "phone": phone.strip(),
                    "department": department
                })
                st.success("Patient registered successfully!")

# VIEW PATIENTS
elif menu == "View Patients":
    st.subheader("Patient Records")

    search = st.text_input("Search patient by name")
    records = list(patients.find())

    if search:
        records = [
            p for p in records
            if search.lower() in p.get("name", "").lower()
        ]

    if records:
        for p in records:
            with st.expander(
                f"{p.get('name', 'Unknown')} — Age: {p.get('age', 'N/A')}"
            ):
                st.write("Patient ID:", str(p["_id"]))
                st.write("Gender:", p.get("gender", "N/A"))
                st.write("Phone:", p.get("phone", "N/A"))
                st.write("Department:", p.get("department", "N/A"))

                with st.form(f"edit_{p['_id']}"):
                    new_name = st.text_input(
                        "Name", value=p.get("name", "")
                    )
                    new_age = st.number_input(
                        "Age", min_value=0, max_value=120,
                        value=int(p.get("age", 0)), step=1
                    )
                    new_phone = st.text_input(
                        "Phone", value=p.get("phone", "")
                    )

                    update = st.form_submit_button("Update Patient")

                    if update:
                        if not new_name.strip() or not new_phone.strip():
                            st.error("Name and phone are required.")
                        else:
                            patients.update_one(
                                {"_id": p["_id"]},
                                {"$set": {
                                    "name": new_name.strip(),
                                    "age": new_age,
                                    "phone": new_phone.strip()
                                }}
                            )
                            st.success("Patient updated. Refresh the page.")

                if st.button("Delete Patient", key=f"del_{p['_id']}"):
                    appointments.delete_many({"patient_id": p["_id"]})
                    patients.delete_one({"_id": p["_id"]})
                    st.success("Patient and related appointments deleted.")
                    st.rerun()
    else:
        st.info("No patient records found.")

# MANAGE DOCTORS
elif menu == "Manage Doctors":
    st.subheader("Doctor Management")

    with st.form("doctor_form"):
        name = st.text_input("Doctor Name")
        specialization = st.selectbox(
            "Specialization",
            ["General Medicine", "Cardiology", "Orthopedics",
             "Neurology", "Pediatrics"]
        )
        experience = st.number_input(
            "Years of Experience", min_value=0, max_value=70, step=1
        )

        submitted = st.form_submit_button("Add Doctor")

        if submitted:
            if not name.strip():
                st.error("Enter the doctor's name.")
            else:
                doctors.insert_one({
                    "name": name.strip(),
                    "specialization": specialization,
                    "experience": experience
                })
                st.success("Doctor added successfully!")

    st.divider()
    st.subheader("Registered Doctors")

    for d in doctors.find():
        st.write(
            f"**{d.get('name', 'Unknown')}** — "
            f"{d.get('specialization', 'N/A')} | "
            f"{d.get('experience', 0)} years experience"
        )

# BOOK APPOINTMENT
elif menu == "Book Appointment":
    st.subheader("Book an Appointment")

    patient_list = list(patients.find())
    doctor_list = list(doctors.find())

    if not patient_list:
        st.warning("Register a patient first.")
    elif not doctor_list:
        st.warning("Add a doctor first.")
    else:
        patient_options = {
            f"{p.get('name', 'Unknown')} ({str(p['_id'])[-6:]})": p
            for p in patient_list
        }
        doctor_options = {
            f"{d.get('name', 'Unknown')} ({d.get('specialization', 'N/A')})": d
            for d in doctor_list
        }

        with st.form("appointment_form"):
            selected_patient = st.selectbox(
                "Select Patient", list(patient_options.keys())
            )
            selected_doctor = st.selectbox(
                "Select Doctor", list(doctor_options.keys())
            )
            appointment_date = st.date_input(
                "Appointment Date", min_value=date.today()
            )
            submitted = st.form_submit_button("Book Appointment")

            if submitted:
                p = patient_options[selected_patient]
                d = doctor_options[selected_doctor]

                appointments.insert_one({
                    "patient_id": p["_id"],
                    "patient_name": p["name"],
                    "doctor_id": d["_id"],
                    "doctor_name": d["name"],
                    "date": appointment_date.isoformat(),
                    "status": "Scheduled"
                })
                st.success("Appointment booked successfully!")

# VIEW APPOINTMENTS
elif menu == "View Appointments":
    st.subheader("Appointment Records")

    for a in appointments.find().sort("date", 1):
        with st.expander(
            f"{a.get('date', 'N/A')} — {a.get('patient_name', 'Unknown')}"
        ):
            st.write("Doctor:", a.get("doctor_name", "N/A"))
            st.write("Status:", a.get("status", "Scheduled"))

            status = st.selectbox(
                "Update Status",
                ["Scheduled", "Completed", "Cancelled"],
                index=["Scheduled", "Completed", "Cancelled"].index(
                    a.get("status", "Scheduled")
                ),
                key=f"status_{a['_id']}"
            )

            if st.button("Save Status", key=f"save_{a['_id']}"):
                appointments.update_one(
                    {"_id": a["_id"]},
                    {"$set": {"status": status}}
                )
                st.success("Appointment status updated.")
                st.rerun()


# REPORTS & ANALYTICS
elif menu == "Reports & Analytics":
    st.subheader("Hospital Reports & Analytics")

    st.write("### Appointments by Doctor")

    pipeline = [
        {
            "$group": {
                "_id": "$doctor_name",
                "total_appointments": {"$sum": 1}
            }
        },
        {"$sort": {"total_appointments": -1}}
    ]

    results = list(appointments.aggregate(pipeline))

    if results:
        for result in results:
            doctor = result["_id"] or "Unknown"
            total = result["total_appointments"]

            st.metric(doctor, total)
    else:
        st.info("No appointments available for analysis.")

    st.divider()
    st.write("### Appointments by Status")

    status_pipeline = [
        {
            "$group": {
                "_id": "$status",
                "total": {"$sum": 1}
            }
        }
    ]

    status_results = list(appointments.aggregate(status_pipeline))

    if status_results:
        for result in status_results:
            st.write(
                f"**{result['_id']}:** {result['total']}"
            )
    else:
        st.info("No appointment status data available.")
