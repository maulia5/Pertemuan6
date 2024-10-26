class Order:
    def __init__(self, id, name, details):
        self.id = id
        self.name = name
        self.details = details
        self.deliveries = []

    def lihatorder(self):
        print(f"ID Pesanan: {self.id}")
        print(f"Nama Pelanggan: {self.name}")
        print(f"Detail Pesanan: {self.details}")
        for delivery in self.deliveries:
            print(f"- Nama Penerima: {delivery.name}")
            print(f"- Tanggal Pengiriman: {delivery.date}")
            print(f"- Alamat Pengiriman: {delivery.address}")
    
def setOrder():
    id = input("Masukkan ID Pesanan: ")
    name = input("Masukkan Nama Pesanan: ")
    details = input("Masukkan Detail Pesanan: ")

    order = Order(id, name, details)
    orders.append(order)
    print("Pesanan anda akan diproses")
    return order
    
def lihat_orders():
    if not orders:
        print("Belum ada pesanan.")
    else:
        for order in orders:
            order.lihatorder()   

def add_delivery(self, delivery):
    self.deliveries.append(delivery)

orders = []

class Delivery:
    def __init__(self, name, date, address):
        self.name = name 
        self.date = date
        self.address = address

def processDelivery():
    name = input("Masukkan Nama Penerima: ")
    date = input("Masukkan Tanggal Pengiriman (YYYY-MM-DD): ")
    address = input("Masukkan Alamat Pengiriman: ")
        
    delivery = Delivery(name, date, address)
    orders.add_delivery(delivery)
    print("Pesanan anda sedang dalam proses pengiriman")


def tampilanmenu():
    while True:
        print("="*10 +"Belanja"+ "="*10)
        print("1. Masukkan Pesanan")
        print("2. Lihat Pesanan")
        print("3. Pengiriman")
        print("4. Keluar")
        pilih  = input("Masukkan pilihan 1/2/3/4:")

        if pilih == '1':
            setOrder()

        if pilih == '2':
            lihat_orders()
        
        if pilih == '3':
            processDelivery()

        if pilih == '4':
            print("Terima kasih telah menggunakan program ini!")
            break

        else:
            print("\n")

tampilanmenu()