/// <reference types="Cypress" />

describe("Tests Navigation", () => {
  it("Exists", () => {
    cy.visit("http://localhost:3000/");
    cy.get("input[data-cy=navigation]").contains("Algorithms");
  });
});
