async function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");

    let userMsg = input.value;
    if(!userMsg) return;

    //Show user message
    chatBox.innerHTML += <div class="user-msg">👤: ${userMsg}</div>
    input.value="";

    //Send to backend
    let response = await fetch("http://127.0.0.1:5000/chat",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body: JSON.stringify({message:userMsg})
    });

    let data =await response.json();
    let botreply = data.reply;

    //Show bot message
    chatBox.innerHTML += <div class="bot-msg">🤖:${botReply}</div>;
    chatBox.scrolltop = chatBox.scrollHeight;

}

async function listenVoice() {
  const res = await fetch("http://127.0.0.1:5000/listen");
  const data = await res.json();

  appendMessage("🎙️ You (voice)", data.recognized_text);

  // Send converted text to chatbot
  const chatRes = await fetch("http://127.0.0.1:5000/chat", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ message: data.recognized_text })
  });

  const replyData = await chatRes.json();
  appendMessage("🤖 RIMT Bot", replyData.reply);
}
