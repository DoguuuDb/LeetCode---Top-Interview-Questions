class Solution:
    # Fonksiyon, tekrarlanmayan en uzun karakter dizisinin uzunluğunu hesaplar
    # @param s: Giriş karakter dizisi
    # @return: Bir tamsayı, en uzun tekrarlanmayan karakter dizisinin uzunluğunu temsil eder
    def lengthOfLongestSubstring(self, s):
        # start, en uzun tekrarlanmayan alt dizenin başlangıcını belirler
        # maxLength, şu ana kadar bulunan en uzun tekrarlanmayan alt dizenin uzunluğunu saklar
        start = maxLength = 0
        # usedChar, kullanılmış karakterleri ve son görüldükleri indeksleri takip eden Dictionary tipinde bir değişkendir.
        usedChar = {} 
        for i in range(len(s)):
            # Eğer karakter zaten kullanıldıysa ve şu anki alt dize içinde bulunuyorsa
            if s[i] in usedChar and start <= usedChar[s[i]]:
                # Başlangıcı tekrarlanan karakterin bir sonraki indeksi ile güncelle.
                start = usedChar[s[i]] + 1
            else:
                # En uzun tekrarlanmayan karakter dizesini güncelle.
                maxLength = max(maxLength, i - start + 1)

            # Kullanılan karakterin son görüldüğü indeksi güncelle.
            usedChar[s[i]] = i
        return maxLength # Sonuç olarak en uzun tekrarlanmayan alt dizenin uzunluğunu döndür
