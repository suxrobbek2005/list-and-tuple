# List and Tuple

---

### **1. Variable va Identifier**
1. `x` o'zgaruvchisini yaratib, unga 5 qiymatini bering. Keyin yangi bir o'zgaruvchi yaratib, `x`ning qiymatini unga saqlang.
2. 3 ta yangi o'zgaruvchi yarating, ularga o'z familiyangiz, ismingiz va yoshingizni saqlang. Ularning nomlarini quyidagicha belgilang: `surname`, `name`, `age`.
3. Noto'g'ri identifier nomlari bilan kod yozing va nima uchun xato ekanini tushuntiring.
4. Uchta turli-tuman qiymatga ega o'zgaruvchi yarating. Keyin biror shart asosida (`if` operatoridan foydalaning), ularning qiymatlarini almashtiring. Oxirida barcha o'zgaruvchilarni chop eting.

---

### **2. Non-primitive Data Types**
1. Biror ro'yxat yarating (`list`), unda 5 ta element bo'lsin. Bu elementlarning turi turli-tuman bo'lsin (masalan, butun son, qator, float).
2. Biror tuple yarating, unda 3 ta element bo'lsin. Bu elementlar list ichida joylashgan bo'lsin.
3. Bir nechta `list` ichida `tuple`lar saqlang. Har bir `tuple`da kamida 3 ta element bo'lsin. Har bir `list`ning ikkinchi `tuple` elementidagi biror qiymatni o'zgartirishga harakat qiling va natijani tushuntiring.

---

### **3. Mutable vs Immutable**
1. Biror ro'yxat yarating va uning biror elementini o'zgartiring. Keyin bu ro'yxatni chop eting.
2. Biror tuple yarating va uning biror elementini o'zgartirishga harakat qiling. Natijani tushuntiring.
3. Quyidagi talablarni bajaradigan kod yozing:
  1. Bir `list` yarating va uning elementlari yordamida yangi `tuple` hosil qiling.  
  2. Ushbu `tuple` elementlarini qayta `list`ga aylantiring va ulardan birini o'zgartiring. 

---

### **4. List**
1. 10 ta butun sondan iborat ro'yxat yarating va uni chop eting.
2. Ro'yxatga oxiriga yangi element qo'shing. Keyin boshlang'ich elementni olib tashlang.
3. 10 ta elementdan iborat `list` yarating. Keyin quyidagi ishlarni bajaring:
  1. Ro'yxatdagi barcha manfiy elementlarni olib tashlang.  
  2. Katta harf bilan yozilgan barcha string elementlarni kichik harfga aylantiring.

---

### **5. List Indexing**
1. 5 ta string elementlardan iborat ro'yxat yarating va ro'yxatning 2- va 4-elementlarini chop eting.
2. Ro'yxatning oxirgi elementini indeks orqali chop eting.
3. 7 ta elementdan iborat `list` yarating. Undagi birinchi, oxirgi va markazdagi elementlarni bir vaqtning o'zida chop eting (`index`dan foydalaning).

---

### **6. List Slicing**
1. 10 ta elementdan iborat ro'yxat yarating. Undan 2- va 7-elementlar orasidagi bo'limni ajratib chop eting.
2. Ro'yxatning har uchinchi elementini chop eting.
3. 15 ta elementdan iborat `list` yarating. Quyidagilarni bajaring:  
  1. Ro'yxatning dastlabki va oxirgi uchta elementlarini bitta yangi `list`ga saqlang.  
  2. Yangi `list`ni teskari tartibda chop eting.

---

### **7. List va String**
1. Biror stringni oling (masalan, `"Hello World!"`) va uni ro'yxatga ajratib chiqaring (har bir harfni alohida element sifatida).
2. Ro'yxatda biror so'z hosil qilish uchun barcha elementlarni birlashtiring.
3. `"Python programming is amazing!"` qatorini `list`ga aylantiring (so'zlar alohida element bo'lsin). Keyin ushbu ro'yxatdan barcha so'zlarning birinchi harflarini yig'ib, yangi string hosil qiling.

---

### **8. Tuple**
1. 4 ta butun sondan iborat tuple yarating va uni chop eting.
2. Tuplega yangi element qo'shishga harakat qiling va natijasini tushuntiring.
3. 5 ta tupledan iborat `list` yarating, har bir tupleda kamida 3 ta element bo'lsin. Barcha `list` ichidagi bir xil qiymatni qidirib toping va uni chop eting.

---

### **9. Tuple Indexing**
1. 5 ta elementdan iborat tuple yarating va uning 3-elementini chop eting.
2. Oxirgi elementni indeks orqali chop eting.
3. 10 ta elementdan iborat `tuple` yarating. Undan 2- va 8-elementlarni chop eting va ularning yig'indisini hisoblang.

---

### **10. Tuple Slicing**
1. 6 ta elementdan iborat tuple yarating va uning faqat birinchi uchta elementini chop eting.
2. Tupledan faqat oxirgi ikki elementni chop eting.
3. 12 ta elementdan iborat `tuple` yarating. Undagi faqat juft indeksli elementlarni tanlab chop eting.

---

### **11. Tuple Methods**
1. Tuple ichida 5 ta element bo'lsin va bu elementlardan biri bir necha marta takrorlangan bo'lsin. `count()` metodidan foydalanib, bu element necha marta qatnashganini toping.
2. Tuple ichida biror elementni `index()` metodidan foydalanib toping.
3. Quyidagi ishlarni bajaring:  
  1. Tuple ichida takrorlanuvchi elementlarni `count()` yordamida aniqlang.  
  2. Shu tuple ichidan eng ko'p takrorlangan elementni toping.  

---

Mana, o'tilgan barcha mavzularga oid aralashtirilgan 10 ta mashq:  

---

### **1.**
- 7 ta elementdan iborat `list` yarating, unda har xil turdagi elementlar (butun son, qator, float va boshqalar) bo'lsin.  
  1. Ro'yxatdagi barcha string elementlarni katta harfga aylantiring.  
  2. Yangi string elementlarni yangi ro'yxatga saqlang.  

---

### **2.**
- `"Learning Python is fun!"` qatoridan foydalanib:  
  1. Har bir so'zni alohida element sifatida ro'yxatga ajrating.  
  2. Ushbu ro'yxatni `tuple`ga aylantiring va oxirgi so'zning indeksini toping.  

---

### **3.**
- Quyidagi qadamlarni bajaring:  
  1. 10 ta elementdan iborat ro'yxat yarating. Har uchinchi elementni teskari tartibda yangi ro'yxatga oling.  
  2. Yangi ro'yxatni `tuple`ga aylantiring va biror elementni qidirib uning indeksini toping.  

---

### **4.**
- Biror `tuple` yarating (kamida 6 ta elementdan iborat). Quyidagilarni bajaring:  
  1. Tupledan 2- va 5-elementlarni oling.  
  2. Ushbu elementlarni birlashtirib string hosil qiling.  

---

### **5.**
- Quyidagi talablarni bajaring:  
  1. 5 ta elementdan iborat tuple yarating va unda 2 ta bir xil element bo'lsin.  
  2. Ushbu tupledagi takrorlanayotgan elementning sonini `count()` bilan toping.  
  3. Natijani chop eting.  

---

### **6.**
- Bir nechta ro'yxatdan iborat ro'yxat (`list`) yarating. Har bir ichki ro'yxat kamida 4 ta elementdan iborat bo'lsin.  
  1. Har bir ichki ro'yxatning oxirgi elementini oling va yangi ro'yxat hosil qiling.  
  2. Yangi ro'yxatni `tuple`ga aylantiring.  

---

### **7.**
- `"Python and data structures are interesting!"` qatorini oling:  
  1. Qatorni faqat harflarga bo'ling (`list` yarating).  
  2. Har bir harfni kichik yoki katta ekanini tekshirib, faqat kichik harflarni yangi ro'yxatga saqlang.  

---

### **8.**
- Quyidagi qadamlarni bajaring:  
  1. 8 ta elementdan iborat `tuple` yarating.  
  2. Tuplening faqat toq indeksdagi elementlarini tanlab yangi tuple yarating.  

---

### **9.**
- Quyidagi qadamlarni bajaring:  
  1. 6 ta elementdan iborat `list` yarating, oxirgi element o'zgarmas tur (immutable) `tuple` bo'lsin.  
  2. Ro'yxatning oxirgi elementini chop eting va uning ichidan biror qiymatni oling.  

---

### **10.**
- 12 ta elementdan iborat ro'yxat yarating, unda sonlar va qatorlar aralashgan bo'lsin.  
  1. Faqat sonlarni tanlab yangi ro'yxat yarating.  
  2. Ushbu ro'yxatdagi elementlarni o'sish tartibida saralang va oxirgi uchta elementni chop eting.  

---