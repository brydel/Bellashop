document.addEventListener('DOMContentLoaded', function () {

  function changeImage(element) {
    var mainProductImage = document.getElementById('mainImage');
    if (mainProductImage) {
      mainProductImage.src = element.src;
    }

    var thumbnails = document.getElementsByClassName('thumbnail');
    for (var i = 0; i < thumbnails.length; i++) {
      thumbnails[i].firstChild.classList.remove('active');
    }

    element.classList.add('active');
  }

  document.querySelectorAll('.dropdown-submenu .dropdown-toggle').forEach(item => {
    item.addEventListener('click', function (event) {
      event.preventDefault();
      event.stopPropagation();
      if (this.nextElementSibling.style.display === 'block') {
        this.nextElementSibling.style.display = 'none';
      } else {
        this.nextElementSibling.style.display = 'block';
      }
    });
  });

  var loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', function (event) {
      event.preventDefault();
      var email = document.getElementById('inputEmail').value;
      var password = document.getElementById('inputPassword').value;

      if (email.trim() === "" || password.trim() === "") {
        alert("Both email and password are required");
        return;
      }

      this.submit();
    });
  }

  // Remplacez ceci par votre propre code de bouton PayPal.
  // paypal.Buttons({...}).render('#paypal-button-container');

  var registrationForm = document.getElementById('registrationForm');
  if (registrationForm) {
    registrationForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirmPassword').value;

      if (password !== confirmPassword) {
        alert("Passwords do not match.");
        return;
      }

      alert('Form is valid and ready to be submitted!');
    });
  }

  var resetPasswordForm = document.getElementById('resetPasswordForm');
  if (resetPasswordForm) {
    resetPasswordForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const email = document.getElementById('emailAddress').value;

      if (!email) {
        alert("Please enter a valid email address.");
        return;
      }

      alert('If an account exists for ' + email + ', a reset link will be sent.');
    });
  }

  var newPasswordForm = document.getElementById('newPasswordForm');
  if (newPasswordForm) {
    newPasswordForm.addEventListener('submit', function (event) {
      event.preventDefault();
      const password = document.getElementById('password').value;
      const confirmPassword = document.getElementById('confirmPassword').value;

      if (!password || password !== confirmPassword) {
        alert("Passwords do not match or are blank.");
        return;
      }

      alert('Password has been successfully reset.');

      this.reset();
      location.href = 'login.html';
    });
  }

  const footerToggler = document.querySelector('.footer-toggler');
  if (footerToggler) {
    const footerContent = document.querySelector('#footerContent');
    footerContent.addEventListener('show.bs.collapse', function () {
      footerToggler.innerHTML = '<i class="fas fa-chevron-circle-down"></i>';
    });

    footerContent.addEventListener('hide.bs.collapse', function () {
      footerToggler.innerHTML = '<i class="fas fa-chevron-circle-up"></i>';
    });
  }

});
// Code original pour la gestion de l'événement submit sur le formulaire avec id 'newAddressForm'
document.getElementById('newAddressForm').addEventListener('submit', function(event) {
  event.preventDefault();
  alert('New address added.');
  this.reset();
});

// Converti pour écouter un clic sur les éléments avec la classe 'btn-secondary'
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.btn-secondary').forEach(function(button) {
      button.addEventListener('click', function() {
          // Code à exécuter lorsqu'un élément avec la classe 'btn-secondary' est cliqué
      });
  });
});

// Converti pour écouter un clic sur les éléments avec la classe 'btn-danger'
document.addEventListener('DOMContentLoaded', function() {
  document.querySelectorAll('.btn-danger').forEach(function(button) {
      button.addEventListener('click', function() {
          // Code à exécuter lorsqu'un élément avec la classe 'btn-danger' est cliqué
      });
  });
});

