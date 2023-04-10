const { buildContact, getIndexOfContact } = require("../helpers");

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

function getContacts(req, res) {
  return res.json(contacts);
}

function getContactById(req, res) {
  const contactIndex = getIndexOfContact(req, contacts);

  if (contactIndex !== -1) {
    return res.json(contacts[contactIndex]);
  }

  return res.status(404).end("Contact not found");
}

function createContact(req, res) {
  const { name, phone } = req.body;

  if (!name || !phone) {
    return res.status(400).json();
  }

  const contact = buildContact(name, phone);

  contacts.push(contact);

  return res.status(201).json(contact);
}

function updateContact(req, res) {
  const { name, phone } = req.body;

  const index = getIndexOfContact(req, contacts);

  if (index === -1) {
    return res.status(404).json({ error: "Contact not found" });
  }

  const contact = contacts[index];
  contact.name = name || contact.name;
  contact.phone = phone || contact.phone;

  return res.status(200).json(contact);
}

function toggleFavorite(req, res) {
  const index = getIndexOfContact(req, contacts);

  if (index === -1) {
    return res.status(404).json({ error: "Contact not found" });
  }

  const contact = contacts[index];
  contact.favorite = !contact.favorite;

  return res.status(200).json(contact);
}

module.exports = {
  getContacts,
  getContactById,
  createContact,
  updateContact,
  toggleFavorite,
};
