const express = require("express");
const app = express();
const http = require("http");
const server = http.createServer(app);
const { Server } = require("socket.io");
const { addUser, removeUser, getUsers, getUser, addMessage, getMessages } = require("./userModule");
const io = new Server(server);

app.get("/", (req, res) => {
  res.sendFile(__dirname + "/index.html");
});

io.on("connection", (socket) => {
  socket.on("set nickname", (id, user) => {
    addUser(id, user);
    console.log(`${getUser(socket.id).nickname} connected`)

    io.emit('userConnected', getMessages());
  });

  socket.on("disconnect", () => {
    removeUser(socket.id);
    console.log(`${getUser(socket.id).nickname} disconnected`)
  });

  socket.on("chat message", (msg) => {
    io.emit("chat message", `${getUser(socket.id).nickname}: ${msg}`, getMessages());
    addMessage(socket.id, msg)
  });
});

server.listen(3000, () => {
  console.log("listening on *:3000");
});
