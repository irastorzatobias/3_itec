const express = require("express");
const { buildContact, getIndexOfContact } = require("./helpers");
const router = express.Router();

let contacts = [
  {
    id: 1,
    date: "2019-05-30T19:20:14.298Z",
    favorite: true,
    name: "juan",
    phone: "66666666",
  },
  {
    id: 2,
    date: "2019-05-30T19:20:14.298Z",
    favorite: true,
    name: "maria",
    phone: "76767676",
  },
];

router.get("/", (req, res) => {
  return res.json(contacts);
});

router.get("/:id", (req, res) => {
  const contactIndex = getIndexOfContact(req, contacts);

  if (contactIndex !== -1) {
    return res.json(contacts[contactIndex]);
  }

  return res.status(404).end("Contact not found");
});

router.post("/", (req, res) => {
  const { name, phone } = req.body;

  if (!name || !phone) {
    return res.status(400).json();
  }

  const contact = buildContact(name, phone);

  contacts.push(contact);

  return res.status(201).json(contact);
});

router.put("/:id", (req, res) => {
  const { name, phone } = req.body;

  const index = getIndexOfContact(req, contacts);

  if (index === -1) {
    return res.status(404).json({ error: "Contact not found" });
  }

  const contact = contacts[index];
  contact.name = name || contact.name;
  contact.phone = phone || contact.phone;

  return res.status(200).json(contact);
});

router.put("/:id/favorite", (req, res) => {
  const index = getIndexOfContact(req, contacts);

  if (index === -1) {
    return res.status(404).json({ error: "Contact not found" });
  }

  const contact = contacts[index];
  contact.favorite = !contact.favorite;

  return res.status(200).json(contact);
});

module.exports = { router };
