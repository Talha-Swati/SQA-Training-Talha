describe('Add multiple products from fixture', () => {
  it('adds all products from fixture to cart', () => {
    cy.login('standard_user', 'secret_sauce');

    cy.fixture('products').then((products) => {
      products.forEach((productName) => {
        const slug = productName.toLowerCase().replace(/\s+/g, '-');
        cy.get(`[data-test="add-to-cart-${slug}"]`).click();
      });

      cy.get('.shopping_cart_badge').should('contain', products.length);
    });
  });
});
