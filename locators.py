from selenium.webdriver.common.by import By

class TestLocators:
    
    # Форма регистрации
    REG_Name_Input = (By.XPATH, ".//input[@name = 'name']") #Поле ввода имени в форме регистрации
    REG_Email_Input = (By.XPATH, "(.//input[@name = 'name'])[2]") #Поле ввода email в форме регистрации
    REG_Password_Input = (By.XPATH, ".//input[@name = 'Пароль']") #Поле ввода пароля в форме регистрации
    REG_Button = (By.XPATH, ".//form/button[text() = 'Зарегистрироваться']") #Кнопка Зарегистрироваться в форме регистрации 
    REG_Password_Error = (By.XPATH, ".//p[text() = 'Некорректный пароль']") #Ошибка некорректного пароля в форме регистрации

    #Форма входа
    LOGIN_Email_Input = (By.XPATH, ".//input[@name='name']") #Поле ввода email в форме авторизации
    LOGIN_Password_Input = (By.XPATH, ".//input[@name='Пароль']") #Поле ввода пароля в форме авторизации
    LOGIN_Button = (By.XPATH, ".//button[text() = 'Войти']") #Кнопка входа в форме авторизации

    # Кнопки авторизации
    LOGIN_Main_Button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']") #Кнопка 'Войти в аккаунт' на главной странице
    LOGIN_Personal_Cabinet_Button = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка 'Личный кабинет'
    LOGIN_Form_Registration = (By.XPATH, ".//a[text() = 'Войти']") #Кнопка 'Войти' в форме регистрации
    LOGIN_Password_Recovery_Form = (By.XPATH, ".//a[text() = 'Войти']") #Кнопка 'Войти' в форме восстановления пароля

    #Кнопка оформления заказа
    MAIN_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")

    # Переходы
    GOTO_Personal_Cabinet_Button = (By.XPATH, ".//p[text() = 'Личный Кабинет']") #Кнопка перехода в личный кабинет
    GOTO_Constructor_Button = (By.XPATH, ".//p[text() = 'Конструктор']") #Кнопка переход в Конструктор
    GOTO_Logo_Button = (By.XPATH, ".//a[@href='/']") #Клик по логотипу

    #Выход
    LOGOUT_profile_button =(By.XPATH, ".//button[text() = 'Выход']") #Кнопка выхода из профиля в личном кабинете

    #Разделы конструктора
    SECTION_Buns = (By.XPATH, ".//span[text() = 'Булки']/parent::div") #Кнопка раздела Булки
    SECTION_Sauces = (By.XPATH, ".//span[text() = 'Соусы']/parent::div") #Кнопка раздела соусы
    SECTION_Fillings = (By.XPATH, ".//span[text() = 'Начинки']/parent::div") #Кнопка раздела Начинки




