const express = require("express");

const app = express();
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    service: "SkillfyBank Account Service",
    status: "running"
  });
});

app.get("/health", (req, res) => {
  res.status(200).json({ status: "healthy" });
});

app.get("/accounts", (req, res) => {
  res.json([
    { id: 1, name: "Demo Customer", balance: 5000 }
  ]);
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, "0.0.0.0", () => {
  console.log(`Account Service listening on port ${PORT}`);
});
