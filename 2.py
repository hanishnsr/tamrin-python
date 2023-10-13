person = {
    "Firstname":"Hanie",
    "Lastname":"Nasrollahi",
    "age":"21",
    "Field": "Computer",
    "Nationalcode":"0372377483"
}
del person["age"]
print(person)
#بله حذف میشود

list=["Massi","52","qom","shahrake qods"]
del list[2]
print(list)
# بله حذف عنصر در لیست ، با استفاده از اندیس امکان پذیر است


my_tuple=("Helen","Shayeste","19.75")
print(my_tuple)
#خیر امکان حذف یک عنصر وجود ندارد. فقط می‌توانیم کل تاپل را حذف کنیم