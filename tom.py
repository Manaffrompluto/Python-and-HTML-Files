import tkinter as tk
from tkinter import ttk, messagebox

class st:
    def __init__(self, w):
        self.w = w
        self.w.title("Stationary Order")
        self.sit = {"Pencil": 0.10, "Pen": 0.25, "Colour Pencil Box": 3, "Oil Pastel Box": 5, "Eraser": 0.10, "Sharpener": 0.25, "Scale": 0.15}
        self.er = 124
        self.setup_background(w)
        f = ttk.Frame(w)
        f.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        ttk.Label(f, text="Stationary Order Management", font=("Arial", 20, "bold")).grid(row=0, columnspan=3, padx=10, pady=10)

        self.sl = {}
        self.sq = {}

        for i, (item, price) in enumerate(self.sit.items(), start=1):
            label = ttk.Label(
                f,
                text=f"{item} (${price}):",
                font=(12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.sl[item] = label

            qe = ttk.Entry(f, width=5)
            qe.grid(row=i, column=1, padx=10, pady=5)
            self.sq[item] = qe

        self.currency_var = tk.StringVar()
        ttk.Label(f, text="Currency:", font=(12)).grid(row=len(self.sit) + 1, column=0, padx=10, pady=5)

        currency_dropdown = ttk.Combobox(f, textvariable=self.currency_var, state="readonly", width=18, values=("USD", "BDT"))
        currency_dropdown.grid(
            row=len(self.sit) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)
        self.currency_var.trace("w", self.update_menu_prices)

        ob = ttk.Button(f,text="Place Order", command=self.place_order)
        ob.grid(row=len(self.sit) + 2, columnspan=3, padx=10, pady=10)

    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()


    def update_menu_prices(self):
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.exchange_rate if currency == "BDT" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "৳" if currency == "BDT" else "$"
        rate = self.er if currency == "BDT" else 1

        for item, entry in self.sq.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.sit[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("ORDER AT LEAST ONE ITEM")

if __name__ == "__main__":
    r = tk.Tk()
    app = st(r)
    r.geometry("800x600")
    r.mainloop()