async function HackingFunction() {
    let timeout;
    for (let i = 0; i <= 100; i++) {
        timeout = Math.floor(Math.random()*90);
        await new Promise((resolve) => setTimeout(resolve, timeout*timeout));
        console.log(`Hacking... ${i}%`);
    }
    console.log("Hacking Completed!");
}

HackingFunction();

