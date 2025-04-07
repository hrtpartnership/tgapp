const tg = Telegram.WebApp;

// Инициализация
tg.expand();
tg.BackButton.show();

// Обработчики
document.getElementById('submit-btn').addEventListener('click', () => {
    const inputText = document.getElementById('user-input').value;
    
    if (inputText.trim()) {
        tg.sendData(JSON.stringify({
            action: "user_message",
            text: inputText,
            timestamp: new Date().toISOString()
        }));
        tg.close();
    }
});

// Кнопка "Назад"
tg.BackButton.onClick(() => tg.close());