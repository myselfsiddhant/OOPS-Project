import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
EMAIL_ADDRESS = "dpssiddhant123@gmail.com"
EMAIL_PASSWORD = "wtde lbir zgwz yixq"  

class Doctor:
    def __init__(self, id, name, specialization):
        self.id = id
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"{self.name} ({self.specialization})"

class Patient:
    def __init__(self, aadhar_number, name, age, sex, disease):
        self.aadhar_number = aadhar_number
        self.name = name
        self.age = age
        self.sex = sex
        self.disease = disease

class Appointment:
    def __init__(self, patient, doctor):
        self.patient = patient
        self.doctor = doctor

    def generate_appointment_details(self):
        details = (f"\n**Appointment Details**\n"
                   f"Patient Name: {self.patient.name}\n"
                   f"Adhaar Number: {self.patient.aadhar_number}\n"
                   f"Age: {self.patient.age}\n"
                   f"Sex: {self.patient.sex}\n"
                   f"Disease: {self.patient.disease}\n"
                   f"Doctor: {self.doctor.name}\n"
                   f"Specialization: {self.doctor.specialization}\n")
        return details

class AppointmentSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Appointment Booking System")
        self.users = {"user@example.com": {"password": "password", "name": "John Doe", "mobile": "1234567890"}}  
        self.current_user = None

        # Initialize doctors
        self.doctors = [
            Doctor(1, "Dr. Rohan", "Cardiology"),
            Doctor(2, "Dr. Kartik", "Neurology"),
            Doctor(3, "Dr. Rohit", "Orthopedics"),
            Doctor(4, "Dr. Arya", "General Physician (Fever, Cough)"),
            Doctor(5, "Dr. Chetan", "Dermatology (Skin Issues)"),
            Doctor(6, "Dr. Aditya", "Pediatrics (Child Health)"),
            Doctor(7, "Dr. Amit Sharma", "ENT (Ear, Nose, Throat)"),
            Doctor(8, "Dr. Saroj Verma", "Gynecology (Women's Health)")
        ]

        self.create_login_screen()

    def create_login_screen(self):
        self.clear_screen()

        # Login Frame
        login_frame = tk.Frame(self.root, padx=10, pady=10)
        login_frame.pack(padx=10, pady=10)

        tk.Label(login_frame, text="Email:").grid(row=0, column=0, pady=5)
        tk.Label(login_frame, text="Password:").grid(row=1, column=0, pady=5)

        self.email_entry = tk.Entry(login_frame)
        self.password_entry = tk.Entry(login_frame, show="*")

        self.email_entry.grid(row=0, column=1, pady=5)
        self.password_entry.grid(row=1, column=1, pady=5)

        login_button = tk.Button(login_frame, text="Login", command=self.login)
        signup_button = tk.Button(login_frame, text="Sign Up", command=self.create_signup_screen)

        login_button.grid(row=2, column=0, pady=10)
        signup_button.grid(row=2, column=1, pady=10)

    def create_signup_screen(self):
        self.clear_screen()

        # Signup Frame
        signup_frame = tk.Frame(self.root, padx=10, pady=10)
        signup_frame.pack(padx=10, pady=10)

        tk.Label(signup_frame, text="Username:").grid(row=0, column=0, pady=5)
        tk.Label(signup_frame, text="Email:").grid(row=1, column=0, pady=5)
        tk.Label(signup_frame, text="Password:").grid(row=2, column=0, pady=5)
        tk.Label(signup_frame, text="Mobile Number:").grid(row=3, column=0, pady=5)

        self.signup_username_entry = tk.Entry(signup_frame)
        self.signup_email_entry = tk.Entry(signup_frame)
        self.signup_password_entry = tk.Entry(signup_frame, show="*")
        self.signup_mobile_entry = tk.Entry(signup_frame)

        self.signup_username_entry.grid(row=0, column=1, pady=5)
        self.signup_email_entry.grid(row=1, column=1, pady=5)
        self.signup_password_entry.grid(row=2, column=1, pady=5)
        self.signup_mobile_entry.grid(row=3, column=1, pady=5)

        register_button = tk.Button(signup_frame, text="Register", command=self.signup)
        back_button = tk.Button(signup_frame, text="Back to Login", command=self.create_login_screen)

        register_button.grid(row=4, column=0, pady=10)
        back_button.grid(row=4, column=1, pady=10)

    def login(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        if email in self.users and self.users[email]["password"] == password:
            self.current_user = {"email": email, "name": self.users[email]["name"], "mobile": self.users[email]["mobile"]}
            self.create_main_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid email or password")

    def signup(self):
        username = self.signup_username_entry.get()
        email = self.signup_email_entry.get()
        password = self.signup_password_entry.get()
        mobile = self.signup_mobile_entry.get()

        if email in self.users:
            messagebox.showerror("Sign Up Failed", "Email already registered")
        else:
            self.users[email] = {"password": password, "name": username, "mobile": mobile}
            messagebox.showinfo("Sign Up Successful", "Account created successfully")
            self.create_login_screen()

    def create_main_screen(self):
        self.clear_screen()

        main_frame = tk.Frame(self.root, padx=10, pady=10)
        main_frame.pack(padx=10, pady=10)

        # Display logged-in user
        user_info_frame = tk.Frame(main_frame)
        user_info_frame.grid(row=0, column=0, sticky="e")
        user_label = tk.Label(user_info_frame, text=f"Logged in as: {self.current_user['name']} ({self.current_user['mobile']})")
        user_label.pack(anchor="e")

        # Patient Details
        details_frame = tk.LabelFrame(main_frame, text="Patient Details", padx=10, pady=10)
        details_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

        tk.Label(details_frame, text="Aadhar Number:").grid(row=0, column=0, sticky="e", pady=5)
        tk.Label(details_frame, text="Name:").grid(row=1, column=0, sticky="e", pady=5)
        tk.Label(details_frame, text="Age:").grid(row=2, column=0, sticky="e", pady=5)
        tk.Label(details_frame, text="Sex:").grid(row=3, column=0, sticky="e", pady=5)
        tk.Label(details_frame, text="Disease Details:").grid(row=4, column=0, sticky="e", pady=5)

        self.aadhar_number_entry = tk.Entry(details_frame)
        self.name_entry = tk.Entry(details_frame)
        self.age_entry = tk.Entry(details_frame)
        self.sex_entry = tk.Entry(details_frame)
        self.disease_entry = tk.Entry(details_frame)

        self.aadhar_number_entry.grid(row=0, column=1, pady=5)
        self.name_entry.grid(row=1, column=1, pady=5)
        self.age_entry.grid(row=2, column=1, pady=5)
        self.sex_entry.grid(row=3, column=1, pady=5)
        self.disease_entry.grid(row=4, column=1, pady=5)

        # Doctor Selection
        doctor_frame = tk.LabelFrame(main_frame, text="Choose Doctor", padx=10, pady=10)
        doctor_frame.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

        self.doctor_var = tk.StringVar(self.root)
        self.doctor_var.set(str(self.doctors[0]))  # default value
        self.doctor_menu = tk.OptionMenu(doctor_frame, self.doctor_var, *[str(doctor) for doctor in self.doctors])
        self.doctor_menu.grid(row=0, column=0, pady=5)

        # Book Appointment Button
        self.book_button = tk.Button(main_frame, text="Book Appointment", command=self.book_appointment)
        self.book_button.grid(row=3, column=0, pady=10)

    def book_appointment(self):
        aadhar_number = self.aadhar_number_entry.get()
        name = self.name_entry.get()
        age = self.age_entry.get()
        sex = self.sex_entry.get()
        disease = self.disease_entry.get()
        doctor_info = self.doctor_var.get()

        if not all([aadhar_number, name, age, sex, disease]):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        patient = Patient(aadhar_number, name, age, sex, disease)
        selected_doctor = next((doctor for doctor in self.doctors if str(doctor) == doctor_info), None)
        
        appointment = Appointment(patient, selected_doctor)
        details = appointment.generate_appointment_details()

        # Send appointment details via email
        self.send_email(self.current_user['email'], details)

        messagebox.showinfo("Appointment Booked", details)

    def send_email(self, recipient_email, details):
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = 'Appointment Confirmation'

        msg.attach(MIMEText(details, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            text = msg.as_string()
            server.sendmail(EMAIL_ADDRESS, recipient_email, text)
            server.quit()
            messagebox.showinfo("Email Sent", "Appointment details sent to your email")
        except Exception as e:
            messagebox.showerror("Email Failed", f"Failed to send email: {e}")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Main execution
if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentSystemGUI(root)
    root.mainloop()







