import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

    

def main():
    access_token = 'sl.BGHyOP3tvAoz9dgTDP3mOfFhIpRW9xkHjcaMcCTEGIQN5ok2vyuSYB9IHODx42yR2D_XwLxf4GExpUtGgsQyuVDPMibc_14GegHBG3-hE8US9DigvIgjFk8BFe1_n_0xgIqGBXQ'
    transfer_data = TransferData(access_token)
    
    file_from = input("D:/Dakshiin/WhitHatJr/C101/test_text.txt")
    
    file_to = 'www.dropbox.com/home/Class_Projects'
    
    transfer_data.upload_file(file_from, file_to)
    print("Files has been moved")

main()