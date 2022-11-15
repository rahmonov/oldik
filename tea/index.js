let fs = require("fs");

let start = async () => {
  let choynak = fs
    .readFileSync("./tea/choynak.txt", { encoding: "utf-8" })
    .split("\n");
  let piyola = fs
    .readFileSync("./tea/piyola.txt", { encoding: "utf-8" })
    .split("\n");

  for (let i = 0; i < 18; i++) {
    console.log(choynak[i] + piyola[i]);
  }

  let about = "Qani oldik choydan :) ";
  let len = 0;
  let _abc = setInterval(() => {
    process.stdout.write(about[len]);
    len = len + 1;
  }, 100);

  setTimeout(() => {
    clearInterval(_abc);
  }, 100 * about.length);
};

start();
