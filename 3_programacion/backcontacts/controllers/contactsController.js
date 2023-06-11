// const { buildContact, getIndexOfContact } = require("../helpers");
const { Contact } = require("../models");

async function getContacts(req, res) {
  try {
    return await Contact.findAll().then((contacts) => res.json(contacts));
  } catch {
    res.status(500).json({ error: "Something went wrong" });
  }
}

async function getContactById(req, res) {
  const { id } = req.params;
  try {
    const response = await Contact.findAll({
      where: {
        id: id,
      },
    });

    return res.json(response);
  } catch {
    res.status(404).json({ error: "Error while fetching contact" });
  }
}

async function createContact(req, res) {
  const { name, phone } = req.body;

  if (!name || !phone) {
    return res.status(400).json();
  }

  try {
    const contact = await Contact.create({
      name: name,
      phone: phone,
      favorite: true,
    });

    return res.status(201).json(contact);
  } catch (e) {
    console.log(e);
  }
}

async function updateContact(req, res) {
  const { name, phone } = req.body;

  try {
    await Contact.update(
      { name: name, phone: phone },
      {
        where: {
          id: req.params.id,
        },
      }
    );
    return res.status(200).send(`contact ${req.params.id} updated`);
  } catch {
    res.status(404).send("error while updating contact");
  }
}

async function toggleFavorite(req, res) {
  try {
    const contact = await Contact.findAll({
      where: {
        id: req.params.id,
      },
    });

    const reverseFavorite = contact[0].favorite ? false : true;

    await Contact.update(
      { favorite: reverseFavorite },
      {
        where: {
          id: req.params.id,
        },
      }
    );

    return res.status(200).json(contact);
  } catch {
    res.status(404).send("error while updating contact");
  }
}

module.exports = {
  getContacts,
  getContactById,
  createContact,
  updateContact,
  toggleFavorite,
};
