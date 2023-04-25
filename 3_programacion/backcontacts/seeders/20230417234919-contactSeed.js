"use strict";

/** @type {import('sequelize-cli').Migration} */
module.exports = {
  async up(queryInterface, Sequelize) {
    /**
     * Add seed commands here.
     *
     * Example:
     * await queryInterface.bulkInsert('People', [{
     *   name: 'John Doe',
     *   isBetaMember: false
     * }], {});
     */
    await queryInterface.bulkInsert(
      "Contacts",
      [
        {
          favorite: false,
          name: "John Doe",
          phone: "3585329897",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          favorite: false,
          name: "Doe john",
          phone: "3585329897",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
        {
          favorite: true,
          name: "Don Juan",
          phone: "358666737",
          createdAt: new Date(),
          updatedAt: new Date(),
        },
      ],
      {}
    );
  },

  async down(queryInterface, Sequelize) {
    /**
     * Add commands to revert seed here.
     *
     * Example:
     * await queryInterface.bulkDelete('People', null, {});
     */
  },
};
