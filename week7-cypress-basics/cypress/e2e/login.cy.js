describe('SauceDemo Login with Fixtures', () => {
  beforeEach(() => {
    cy.fixture('users').as('users');
  });

  it('logs in with valid user', function () {
    cy.login(this.users.validUser.username, this.users.validUser.password);
    cy.url().should('include', 'inventory');
  });

  it('shows error with invalid user', function () {
    cy.login(this.users.invalidUser.username, this.users.invalidUser.password);
    cy.get('[data-test="error"]').should('contain', 'Username and password do not match');
  });

  it('blocks locked out user', function () {
    cy.login(this.users.lockedUser.username, this.users.lockedUser.password);
    cy.get('[data-test="error"]').should('contain', 'Sorry, this user has been locked out');
  });
});
