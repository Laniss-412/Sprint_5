from selenium.webdriver.common.by import By

class TestLocators:
    
    # Регистрация
    REG_Name_Input = (By.XPATH, "(.//input[@name = 'name'])[1]") #Поле ввода имени при регистрации
    REG_Email_Input = (By.XPATH, "(.//input[@name = 'name'])[2]") #Поле ввода email при регистрации
    REG_Password_Input = (By.XPATH, ".//input[@name = 'Пароль']") #Поле ввода пароля при регистрации
    REG_Button = (By.XPATH, ".//form/button[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться  
    REG_Password_Error = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #Ошибка некорректного пароля

    # Авторизация
    LOGIN_Main_Button = (By.XPATH, ".//section/button[text() = 'Войти в аккаунт']") #Вход через кнопку 'Войти в аккаунт' на главной странице
    LOGIN_Personal_Cabinet_Button = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Вход через кнопку 'Личный кабинет'
    LOGIN_Form_Registration = (By.XPATH, ".//a[text() = 'Войти']") #Вход через кнопку 'Войти' в форме регистрации
    LOGIN_Password_Recovery_Form = (By.XPATH, ".//a[text() = 'Войти']") #Вход через кнопку 'Войти' в форме восстановления пароля

    # Переходы
    GOTO_Personal_Cabinet_Button = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка перехода в личный кабинет
    GOTO_Constructor_Button = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка переход в Конструктор
    GOTO_Logo_Button = (By.XPATH, ".//div[contains(@class, 'header__logo')]") #Клик по логотипу

    #Выход
    LOGOUT_profile_button =(By.XPATH, ".//button[text() = 'Выход']") #Кнопка выхода из профиля в личном кабинете

    #Разделы конструктора
    SECTION_Buns = (By.XPATH, ".//span[text() = 'Булки']") #Кнопка раздела Булки
    SECTION_Sauces = (By.XPATH, ".//span[text() = 'Соусы']") #Кнопка раздела соусы
    SECTION_Fillings = (By.XPATH, ".//span[text() = 'Начинки']") #Кнопка раздела Начинки




