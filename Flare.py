import customtkinter as ctk
from tkinter import *
from tkinter import SUNKEN, messagebox
from PIL import Image, ImageTk
import os
import sys

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1026x600")
        self.root.title("Solar_Flare")
        self.root.resizable(False, False)
        
        # First page setup
        self.create_first_page()

    def create_first_page(self):
        #self.second_page.pack_forget()


        # Determine correct base path for assets
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller EXE
            base_path = sys._MEIPASS
        else:  # Running as a normal script
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Construct the correct image path
        home_path = os.path.join(base_path, "assets", "Home.jpg")

        self.page1 = ctk.CTkFrame(self.root)
        self.page1.pack(fill=ctk.BOTH, expand=True)

        self.bg_image = ctk.CTkImage(Image.open(home_path),
                                     size=(1024, 600))
        self.bg_label = ctk.CTkLabel(self.page1, image=self.bg_image, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        def cmd1():
            os.system("sudo shutdown now")
            print("Shutdown")
                
        def cmd2():
            self.show_second_page()
            print("Next Page")
                

        def on_label_hover(e):
            shut_btn.configure(text_color="#141D26", fg_color="#FFFFFF", border_color="#FFFFFF")  # Change text color on hover

        def on_label_leave(e):
            shut_btn.configure(text_color="white",fg_color="#141D26", border_color="#FFFFFF")  # Revert text color on leave

        shut_btn = ctk.CTkButton(self.page1, text="Shutdown", width=177, height=56,
                                    corner_radius=25, fg_color="#141D26", bg_color="#141D26", font=("Poppins", 26, "bold"),
                                    border_color="#FFFFFF", border_width=3,
                                    text_color="white", hover_color="#FFFFFF", command=cmd1)
        shut_btn.place(x=85, y=402)

        # Bind hover events
        shut_btn.bind("<Enter>", on_label_hover)
        shut_btn.bind("<Leave>", on_label_leave)

        prcd_btn = ctk.CTkButton(self.page1, text="Proceed", width=177, height=56,
                                    corner_radius=25, fg_color="#2C2E38", bg_color="#2C2E38", font=("Poppins", 26, "bold"),
                                    border_color="#FD6D22", border_width=3,
                                    text_color="white", hover_color="#FD6D22", command=cmd2)
        prcd_btn.place(x=424, y=402)

    def show_second_page(self):
        self.page1.pack_forget()
        
        root.lift()
        root.focus_force()
        # Create the second page frame
        self.second_page = ctk.CTkFrame(self.root)
        self.second_page.pack(fill="both", expand=True)
        self.root.update()
        # Track active entry field
        active_entry = None

        # Function to set the active entry field when clicked
        def set_active(entry):
            nonlocal active_entry
            active_entry = entry

        # Function to insert text into the active entry
        def insert_text(char):
            if active_entry:
                active_entry.insert("insert", char)

        # Function to delete last character
        def delete_last():
            if active_entry:
                current_pos = active_entry.index("insert")
                if current_pos > 0:
                    active_entry.delete(current_pos - 1, current_pos)

        # Function to switch to the next entry
        def focus_next():
            if active_entry:
                try:
                    index = self.entry_widgets.index(active_entry)
                    next_entry = self.entry_widgets[index + 1]
                    next_entry.focus_set()
                    set_active(next_entry)
                except IndexError:
                    pass  # Do nothing if it's the last field


        
        # Determine correct base path for assets
        if getattr(sys, 'frozen', False):  # Running as a PyInstaller EXE
            base_path = sys._MEIPASS
        else:  # Running as a normal script
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Construct the correct image path
        pg2_path = os.path.join(base_path, "assets", "pg2.jpg")

        # Load and set the background image
        self.bg_image = ctk.CTkImage(Image.open(pg2_path),
                                     size=(1024, 600))
        
        bg_label = ctk.CTkLabel(self.second_page, image=self.bg_image, text="")
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.update()
        # Outer frame with rounded corners
        outer_frame = ctk.CTkFrame(self.second_page, width=500, height=400, corner_radius=5,
                                     border_width=1, bg_color="#252934"
                                   )
        outer_frame.place(x=50, y=120)
        self.root.update()
        scrollable_frame = ctk.CTkScrollableFrame(outer_frame, width=500, height=400,corner_radius=10,
                                                   fg_color="#252934", border_color="#3D3D3D", bg_color="#252934")
        scrollable_frame.pack(padx=2, pady=2, fill="both", expand=True)
        self.root.update()
        #outer_frame.lift(scrollable_frame)
        label_names = ['TOTUSJH', 'TOTBSQ', 'TOTPOT', 'TOTUSJZ', 'SAVNCPP', 'USFLUX', 'TOTFZ',
                        'MEANPOT', 'MEANSHR', 'SHRGT45', 'MEANGBT', 'MEANGBZ', 'MEANALP',
                        'EPSX', 'R_VALUE', 'CRLT_OBS', 'CRVAL2', 'HC_ANGLE', 'SPEI', 'LON_MIN',
                        'LAT_MAX', 'LON_MAX', 'IS_TMFI']
        
        self.entry_widgets = []

        for i, name in enumerate(label_names):
            label = ctk.CTkLabel(scrollable_frame, text=name, font=("Poppins", 16, "bold"), text_color="white")
            label.grid(row=i//2*2, column=i%2, padx=(10,30), pady=(10, 0), sticky="w")
            
            entry = ctk.CTkEntry(scrollable_frame, font=("Poppins", 14),
                                 width=212, height=41, fg_color="white", text_color="black",
                                 corner_radius=15, bg_color="#252934", border_width=0)
            entry.grid(row=i//2*2+1, column=i%2, padx=(10,30), pady=(0, 10), sticky="w")
            entry.bind("<FocusIn>", lambda e, en=entry: set_active(en))
            self.entry_widgets.append(entry)
        
        self.root.update()

        
        # Right panel for buttons
        right_frame = ctk.CTkFrame(self.second_page, width=330, height=280, corner_radius=5, )
        right_frame.place(x=660, y=280)
        right_frame.configure(bg_color="#272935", fg_color="#272935")
        self.root.update()
        #Create a fixed keyboard at the bottom of the right frame
        keyboard_frame = ctk.CTkFrame(right_frame, fg_color="#272935",height=310, width=360)
        keyboard_frame.place(x=9,y=12)
        
        # Keypad layout
        keyboard_layout = [
            ["1", "2", "3", "+"],
            ["4", "5", "6", "-"],
            ["7", "8", "9", "Del"],
            [".", "0", "e", "Next"]
        ]
        
        # Add buttons to the keyboard
        for row in keyboard_layout:
            row_frame = ctk.CTkFrame(keyboard_frame, fg_color="#272935", bg_color="#272935")
            row_frame.pack(anchor="w")
            for key in row:
                if key == "Del":
                    btn = ctk.CTkButton(row_frame, text=key, width=50, height=55, hover_color="#EE6923",
                                        fg_color="#FD6D22", bg_color="#272935",text_color="white", corner_radius=25,
                                        font=("Poppins", 19, "bold"), command=delete_last)
                elif key == "Next":
                    btn = ctk.CTkButton(row_frame, text=key, width=60, height=55, hover_color="white",
                                        fg_color="#272935", bg_color="#272935",text_color="white", corner_radius=25,
                                        border_color="white", border_width=2,
                                        font=("Poppins", 19, "bold"), command=focus_next)
                else:
                    btn = ctk.CTkButton(row_frame, text=key, width=60, height=55, hover_color="white",
                                        fg_color="#272935", bg_color="#272935",text_color="white", corner_radius=25,
                                        border_color="white", border_width=2,
                                        font=("Poppins", 19, "bold"),command=lambda c=key: insert_text(c))
                btn.pack(side="left", padx=4, pady=4)
        self.root.update()

        get_values_btn = ctk.CTkButton(self.second_page, text="Predict", width=110, height=41,
                                    corner_radius=20, fg_color="#26272E", bg_color="#26272E", font=("Poppins", 19, "bold"),
                                    border_color="#FD6D22", border_width=2,
                                    text_color="white", hover_color="#FD6D22", command=self.get_all_entry_values)
        get_values_btn.place(x=676, y=198)

        clear_entries_btn = ctk.CTkButton(self.second_page, text="Clear Entries", width=135, height=41,
                                          border_color="white", border_width=2, corner_radius=20, 
                                          fg_color="#1F2127", bg_color="#1F2127", font=("Poppins", 19, "bold"), text_color="white",
                                          hover_color="white", command=self.clear_all_entries)
        clear_entries_btn.place(x=817, y=198)
 
        self.text_label_out = ctk.CTkLabel(self.second_page, text="Solar Flare", font=("Poppins", 25, "bold"), justify="left", 
                                           anchor="w", text_color="#C1C1C1", fg_color="#F4F4F4", bg_color="#F4F4F4", height=65, width=240)
        self.text_label_out.place(x=705, y=90)
        
        def cmd3():
            self.second_page.pack_forget()
            self.create_first_page()
            
            print("Back Page")

        def on_label_hover(e):
            bck_btn.configure(text_color="#141D26", fg_color="#FFFFFF", border_color="#FFFFFF")  # Change text color on hover

        def on_label_leave(e):
            bck_btn.configure(text_color="white",fg_color="#141D26", border_color="#FFFFFF")  # Revert text color on leave



        bck_btn = ctk.CTkButton(self.second_page, text="<", width=40, height=40,
                                    corner_radius=17, fg_color="#20232C", bg_color="#20232C", font=("Poppins", 18, "bold"),
                                    border_color="white", border_width=2, anchor="e",
                                    text_color="white", hover_color="#FD6D22", command=cmd3)
        bck_btn.place(x=560, y=40)
        self.root.update()

        # Bind hover events
        bck_btn.bind("<Enter>", on_label_hover)
        bck_btn.bind("<Leave>", on_label_leave)
    
    def show_prd(self):
        self.text_label_out.configure(text="Sample", font=("Poppins", 25, "bold"), justify="left", 
                                           anchor="w", text_color="black",)
    
    def show_err(self):
        self.text_label_out.configure(text="Invalid", font=("Poppins", 25, "bold"), justify="left", 
                                           anchor="w", text_color="black",)
        
    def clr_prd(self):
        self.text_label_out.configure(text="Solar Flare", font=("Poppins", 25, "bold"), justify="left", 
                                      anchor="w", text_color="#C1C1C1",)
    
    def get_all_entry_values(self):
        values = [entry.get() for entry in self.entry_widgets] # Array of scientific notation strings
        
        try:
            if not all(values):
                self.show_err()
            
            float_array = [float(num) for num in values]  # Convert non-empty values to float
            #float_array = [float(num) for num in values if num]  # Convert non-empty values to float
            
            import pandas as pd
            import joblib
            import numpy as np

            features_name = ['TOTUSJH', 'TOTBSQ', 'TOTPOT', 'TOTUSJZ', 'SAVNCPP', 'USFLUX', 'TOTFZ', 'MEANPOT', 'MEANSHR', 'SHRGT45', 'MEANGBT', 
                            'MEANGBZ', 'MEANALP', 'EPSX', 'R_VALUE', 'CRLT_OBS', 'CRVAL2', 'HC_ANGLE', 'SPEI', 'LON_MIN', 'LAT_MAX', 'LON_MAX', 'IS_TMFI']
            
            # Determine correct base path for assets
            if getattr(sys, 'frozen', False):  # Running as a PyInstaller EXE
                base_path = sys._MEIPASS
            else:  # Running as a normal script
                base_path = os.path.dirname(os.path.abspath(__file__))

            # Construct the correct model path
            scaler_path = os.path.join(base_path, "assets", "model", "scaler.pkl")
            model_path = os.path.join(base_path, "assets", "model", "KNN_Model_Class.pkl")
            int_path = os.path.join(base_path, "assets", "model", "KNN_Model_Intensity.pkl")

            # Load the saved MinMaxScaler
            scaler = joblib.load(scaler_path)  

            # Convert list to a pandas DataFrame with feature names
            input_df = pd.DataFrame([float_array], columns=features_name)

            # Transform the input using the loaded scaler
            scaled_input = scaler.transform(input_df)
            scaled_input = scaled_input.flatten()
            
            scaled_input = [float(val) for val in scaled_input]

            #print(float_array)  # Debugging
            #print(scaled_input)  # Debugging

            indices= [0, 1, 3, 5, 8, 9, 12, 14, 15, 17, 20, 21]

            # Get the values from usr_inp based on the specified indices
            class_val = [scaled_input[i] for i in indices]
            class_val_cld = [float(val) for val in class_val]
            
            #print(class_val_cld)  # Debugging
            
            features_name_cls = ["TOTUSJH","TOTBSQ","TOTUSJZ","USFLUX","MEANSHR","SHRGT45",
                                 "MEANALP","R_VALUE","CRVAL2","SPEI","LAT_MAX","LON_MAX"]
            
            # Convert input_data to a DataFrame with feature names
            input_df_class = pd.DataFrame([class_val_cld], columns=features_name_cls)

            # Load the saved KNN model
            mdl_class = joblib.load(model_path)
            prediction_class = mdl_class.predict(np.array(scaled_input).reshape(1, -1))

            #print(prediction_class)  # Debugging

            # Define the mapping dictionary
            class_mapping = {
                0: "B",
                1: "C",
                2: "M",
                3: "X",
                4: "NOT a Flare"
            }

            # Save prediction in a variable
            predicted_class_index = prediction_class.item()

            # Get the corresponding class name
            predicted_class_label = class_mapping.get(predicted_class_index, "Unknown")

            if predicted_class_label == "M":
                
                mdl_int = joblib.load(int_path)
                
                # Convert input_data to a DataFrame with feature names
                input_df_int = pd.DataFrame([scaled_input], columns=features_name)
                prediction_int = mdl_int.predict(input_df_int)

                # Define the mapping dictionary
                int_mapping = {
                    0: "M1",
                    1: "M2",
                    2: "M3",
                    3: "M4",
                    4: "M5",
                    5: "M6",
                    6: "M7",
                    7: "M8",
                    8: "M9"
                }

                # Save prediction in a variable
                predicted_int_index = prediction_int.item()

                # Get the corresponding class name
                predicted_int_label = int_mapping.get(predicted_int_index, "Unknown")

                # Print the result
                print(f"Predicted Class: {predicted_int_label}")

                self.text_label_out.configure(text= f"{predicted_int_label} Class", font=("Poppins", 25, "bold"), justify="left", 
                                           anchor="w", text_color="black",)

            else:
                # Print the result
                print(f"Predicted Class: {predicted_class_label}")
                self.text_label_out.configure(text= f"{predicted_class_label} Class", font=("Poppins", 25, "bold"), justify="left", 
                                           anchor="w", text_color="black",)


        except ValueError as e:
            print("Invalid input detected:", e)
            self.show_err()
            print(values)


    def clear_all_entries(self):
        self.clr_prd()
        for entry in self.entry_widgets:
            entry.delete(0, ctk.END)
            
if __name__ == "__main__":
    root = ctk.CTk()
    root.attributes("-fullscreen", True)  # Makes the window fullscreen
    app = MyApp(root)
    # Force the size to 1024x600 after setting fullscreen
    root.geometry("1024x600")
    #root.overrideredirect(True)
    root.mainloop()


