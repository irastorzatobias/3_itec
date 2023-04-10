const express = require("express");
const router = express.Router();
const {
  getContacts,
  getContactById,
  createContact,
  updateContact,
  toggleFavorite,
} = require("../controllers/contactsController");

router.get("/", getContacts);

router.get("/:id", getContactById);

router.post("/", createContact);

router.put("/:id", updateContact);

router.put("/:id/favorite", toggleFavorite);

module.exports = { router };
