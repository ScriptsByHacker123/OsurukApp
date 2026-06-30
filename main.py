import webbrowser

def asistan():
    print("--- AI Asistan Aktif (Çıkmak için 'çık' yaz) ---")
    
    while True:
        # Kullanıcıdan komut al
        komut = input("\nNe çalalım?: ")
        
        # Programdan çıkış şartı
        if komut.lower() == "çık":
            print("Görüşmek üzere!")
            break
            
        # YouTube'da arama yap
        print(f"YouTube'da aranıyor: {komut}")
        url = f"https://www.youtube.com/results?search_query={komut}"
        webbrowser.open(url)

if __name__ == "__main__":
    asistan()
