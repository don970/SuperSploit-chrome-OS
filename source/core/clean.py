class clean:
    def __init__(self, ar):
        with open(".data/.custom_scan", "w") as file:
            file.write(" ")
            file.close()
        with open(".data/.phone_numbers", "w") as file:
            file.write(" ")
            file.close()
        with open(".data/.targeted_scan", "w") as file:
            file.write(" ")
            file.close()
        with open(".data/.targets", "w") as file:
            file.write(" ")
            file.close()
        return