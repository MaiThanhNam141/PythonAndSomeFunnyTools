async function HackingFunction() {
    let timeout;
    for (let i = 0; i <= 100; i++) {
        timeout = Math.floor(Math.random()*100);
        console.log(`Hacking... ${i}%`);
        await new Promise((resolve) => setTimeout(resolve, timeout*timeout));
    }
    console.log("Hacking Completed!");
}

HackingFunction();

