describe('SauceDemo Login', () => {
  it('logs in with valid credentials', () => {
    cy.visit('https://www.saucedemo.com');
    cy.get('#user-name').type('standard_user');
    cy.get('#password').type('secret_sauce');
    cy.get('#login-button').click();
    cy.url().should('include', 'inventory');
  });

  it('shows error with invalid credentials', () => {
    cy.visit('https://www.saucedemo.com');
    cy.get('#user-name').type('wrong_user');
    cy.get('#password').type('wrong_pass');
    cy.get('#login-button').click();
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match');
  });

  it('blocks a locked out user with the correct error message', () => {
    cy.visit('https://www.saucedemo.com');
    cy.get('#user-name').type('locked_out_user');
    cy.get('#password').type('secret_sauce');
    cy.get('#login-button').click();
    cy.get('[data-test="error"]').should('contain', 'Sorry, this user has been locked out');
  });
});
