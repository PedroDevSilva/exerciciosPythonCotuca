const button = document.getElementById("fugitive-btn");
const wrapper = document.querySelector(".button-wrapper");

wrapper.style.position = "relative";
button.style.position = "absolute";

wrapper.addEventListener("mousemove", (e) => {
  const rect = wrapper.getBoundingClientRect();
  const mouseX = e.clientX - rect.left;
  const mouseY = e.clientY - rect.top;

  const btnRect = button.getBoundingClientRect();
  const btnX = button.offsetLeft + button.offsetWidth / 2;
  const btnY = button.offsetTop + button.offsetHeight / 2;

  const distance = Math.hypot(mouseX - btnX, mouseY - btnY);

  if (distance < 80) {
    const offsetX = Math.random() * (wrapper.clientWidth - button.offsetWidth);
    const offsetY = Math.random() * (wrapper.clientHeight - button.offsetHeight);
    button.style.left = `${offsetX}px`;
    button.style.top = `${offsetY}px`;
  }
});
