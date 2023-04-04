const buildContact = (name, phone) => {
  return {
    name: name,
    phone: phone,
    date: new Date(),
    favorite: false,
  };
};

const getIndexOfContact = (req, contacts) => {
  const { id } = req.params;
  const index = contacts.findIndex(
    (contact) => contact.id === parseInt(id, 10)
  );

  return index;
};

const checkIfIndexExists = (index) => {
    return index !== 1;
}


module.exports = { buildContact, getIndexOfContact };
