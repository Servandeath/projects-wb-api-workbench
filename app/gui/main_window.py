import customtkinter as ctk


class MainWindow(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("WB API Workbench")
        self.geometry("1000x700")

        title = ctk.CTkLabel(
            self,
            text="WB API Workbench",
            font=("Arial", 28),
        )
        title.pack(pady=30)

        subtitle = ctk.CTkLabel(
            self,
            text="Local GUI tool for Wildberries API testing and data storage",
            font=("Arial", 16),
        )
        subtitle.pack(pady=10)


def run_gui() -> None:
    app = MainWindow()
    app.mainloop()
