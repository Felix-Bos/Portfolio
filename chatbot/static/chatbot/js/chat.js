document.addEventListener("DOMContentLoaded", function () {
    const chatPopup = document.getElementById("chatbot-popup");
    const closeChatbot = document.getElementById("close-chatbot");
    const sendMessage = document.getElementById("send-message");
    const messageInput = document.getElementById("message-input");
    const chatbotMessages = document.getElementById("chatbot-messages");
    const openChatbotButton = document.getElementById("chat-button");

    function toggleChatbot() {
        chatPopup.classList.toggle("hidden");
    }

    if (openChatbotButton) {
        openChatbotButton.addEventListener("click", toggleChatbot);
    }

    if (closeChatbot) {
        closeChatbot.addEventListener("click", toggleChatbot);
    }

    function addMessage(message, sender) {
        const messageElement = document.createElement("div");
        messageElement.classList.add("message", sender);
        messageElement.textContent = message;
        chatbotMessages.appendChild(messageElement);
        chatbotMessages.scrollTop = chatbotMessages.scrollHeight;
    }

    async function handleSendMessage() {
        const query = messageInput.value.trim();
        if (!query) return;

        addMessage(query, "user");
        messageInput.value = "";

        try {
            const response = await fetch("/chatbot/api/chat/", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ query: query }),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            addMessage(data.answer, "bot");

        } catch (error) {
            console.error("Error sending message:", error);
            addMessage("Sorry, something went wrong.", "bot");
        }
    }

    if (sendMessage) {
        sendMessage.addEventListener("click", handleSendMessage);
    }

    if (messageInput) {
        messageInput.addEventListener("keypress", function (e) {
            if (e.key === "Enter") {
                handleSendMessage();
            }
        });
    }
});