import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

class AddStudent:
    def __init__(self, data_processor):
        self.data_processor = data_processor


    ''' ---------------------------------------------------------------------------------------------------------------
    *
    *
    *   OLD FUNCTIONS FEEL FREE TO REMOVE THESE ARE THEY ARE SUPERSEDED BY THE DATA_PROCESSOR CLASS WHICH HANLES IT NOW
    *
    *
    * ----------------------------------------------------------------------------------------------------------------- '''
    
    def func(self, student):
        pass
        """
        Write a single student to the file.
        """
        self.write(student)

    def create(self, attributes):
        pass
        students_id = []

        for student in self.read():
            print(f"{student.id}")
            students_id.append(student.id)

        name, age, student_id, email, phone = attributes
        new_student = self.constructor(name, age, student_id, email, phone)
        print("Searching if ID is duplicate")
        if new_student.id in students_id:
            print("Duplicate ID Found")
            return -1
        print("Passed, adding student")
        self.func(new_student)
        return 0

    def read(self):
        pass
        try:
            with open(self.path, 'r') as f:
                for line in f:
                    if line.strip():
                        attributes = [value.strip() for value in line.strip().split(',')]
                        print(f"Attributes after split: {attributes}")  # Debugging
                        if len(attributes) == 5:  # Check for proper number of attributes
                            name, age, student_id, email, phone = attributes
                            student = self.constructor(name, age, student_id, email, phone)
                            #print(f"Loaded student: {student.attributes()}")
                            yield student
                        else:
                            print("Warning: Incorrect number of attributes in line.")
        except FileNotFoundError:
            print(f"Error: The file '{self.path}' does not exist.")
        except ValueError as e:
            print(f"Error: Invalid data format in file: {e}")
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")


    def write(self, student):
        pass
        """
        Append a single student to the file.
        """
        try:
            with open(self.path, 'a') as f:
                display = ",".join(student.attributes())
                f.write(f"{display}\n")
                print(f"Student written to file: {display}")
        except Exception as e:
            print(f"An error occurred while writing to the file: {e}")
    '''----------------------------------------------------------------------------------------------------------------- ''' 


    def show_student_ui(self, view_profile_frame, student: object):
        print(f"displaying student {student}:")
        if not student:
            return

        self.label = ctk.CTkLabel(view_profile_frame, text="", font=("Tahoma", 20, "italic"))
        self.label.configure(text=f"{student}")
        self.label.pack(pady=10)

    def show_reg_ui(self, register_frame):
        """
        Create the student registration UI.
        """
        self.lblErrors = ctk.CTkLabel(register_frame, text="", font=("Tahoma", 20, "italic"), text_color="red")
        self.lblErrors.pack(pady=10)  

        self.register_txt = ["Name", "Age", "Student ID", "Email Address", "Phone Number"]
        self.register_entry = []
        for i in range(len(self.register_txt)):
            label = ctk.CTkLabel(register_frame, text=self.register_txt[i], font=("Tahoma", 20), width=13, anchor="e")
            label.pack(pady=5, padx=20, anchor="w")  
            entry = ctk.CTkEntry(register_frame, width=40, font=("Tahoma", 20, "italic"))
            entry.pack(pady=5, padx=20, fill="x") 
            self.register_entry.append(entry)

        register_btn = ctk.CTkButton(register_frame, width=30, text="Register Student",
                                    font=("Tahoma", 20, "italic"), command=self.check_entries)
        register_btn.pack(pady=20)

    def check_entries(self):
        """
        Validate and create a new student from form input.
        """
        errors = []
        for i in range(len(self.register_entry)):
            if not self.register_entry[i].get().strip():  # Check for empty fields
                errors.append(f"You forgot to add the {self.register_txt[i]}!\n")

        if not errors:
            attributes = [
                self.register_entry[0].get().strip(),
                self.register_entry[1].get().strip(),
                self.register_entry[2].get().strip(),
                self.register_entry[3].get().strip(),
                self.register_entry[4].get().strip(),
            ]

            result = self.data_processor.add_student_to_program(*attributes)

            if type(result) == object:
                response = CTkMessagebox(message="The student registration was successful.",
                    icon="check", option_1="Continue")
            
                response_get = response.get()

                if response_get:
                    for entry in self.register_entry:
                        entry.delete(0, ctk.END)
            else:
                self.lblErrors.configure(
                text=f"The Student ID {attributes[2]} is already taken"
            )
        else:
            self.lblErrors.configure(
                text=f"The following error(s) occurred:\n{''.join(errors)}\nPlease try again."
            )