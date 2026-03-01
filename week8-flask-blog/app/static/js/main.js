/* ============================================================
   My Flask Blog — Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ------------------------------------------------------------------
  // Auto-dismiss flash alerts after 5 seconds
  // ------------------------------------------------------------------
  document.querySelectorAll('.alert.alert-dismissible').forEach(alert => {
    setTimeout(() => {
      const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
      bsAlert.close();
    }, 5000);
  });

  // ------------------------------------------------------------------
  // Auto-slugify: title field → slug field on create post page
  // ------------------------------------------------------------------
  const titleInput = document.querySelector('input[name="title"]');
  const slugInput  = document.querySelector('input[name="slug"]');

  function slugify(str) {
    return str
      .toLowerCase()
      .trim()
      .replace(/[^\w\s-]/g, '')
      .replace(/[\s_-]+/g, '-')
      .replace(/^-+|-+$/g, '');
  }

  if (titleInput && slugInput) {
    titleInput.addEventListener('input', () => {
      if (!slugInput.dataset.manualEdit) {
        slugInput.value = slugify(titleInput.value);
      }
    });
    // Mark as manually edited once the user types in slug
    slugInput.addEventListener('input', () => {
      slugInput.dataset.manualEdit = '1';
    });
  }

  // ------------------------------------------------------------------
  // Confirm delete dialogs (data-confirm attribute)
  // ------------------------------------------------------------------
  document.querySelectorAll('[data-confirm]').forEach(el => {
    el.addEventListener('click', e => {
      if (!confirm(el.dataset.confirm)) {
        e.preventDefault();
      }
    });
  });

  // ------------------------------------------------------------------
  // Highlight active nav link
  // ------------------------------------------------------------------
  const currentPath = window.location.pathname;
  document.querySelectorAll('.nav-link').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active');
    }
  });

  // ------------------------------------------------------------------
  // Smooth scroll to #comments anchor
  // ------------------------------------------------------------------
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

});
