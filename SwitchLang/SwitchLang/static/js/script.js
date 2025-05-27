document.addEventListener('DOMContentLoaded', function () {
    const form = document.getElementById('translateForm');
    const loader = document.getElementById('loader');
  
    form.addEventListener('submit', function () {
      loader.classList.remove('hidden');
    });
  });
  