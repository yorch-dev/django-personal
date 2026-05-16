(function () {
  function cleanValue(value) {
    return value.replace(/\D/g, '');
  }

  function formatNumber(value) {
    if (!value) {
      return '';
    }
    const digits = cleanValue(value);
    return digits.replace(/\B(?=(\d{3})+(?!\d))/g, '.');
  }

  function onInput(event) {
    const input = event.target;
    const selectionStart = input.selectionStart;
    const previousLength = input.value.length;
    input.value = formatNumber(input.value);
    const newLength = input.value.length;
    const diff = newLength - previousLength;
    if (selectionStart !== null) {
      input.selectionStart = input.selectionEnd = Math.max(0, selectionStart + diff);
    }
  }

  function removeFormat(input) {
    input.value = cleanValue(input.value);
  }

  document.addEventListener('DOMContentLoaded', function () {
    const fields = document.querySelectorAll('.js-number-with-dots');
    if (!fields.length) {
      return;
    }

    fields.forEach(function (field) {
      field.value = formatNumber(field.value);
      field.addEventListener('input', onInput);
      field.addEventListener('blur', function () {
        field.value = formatNumber(field.value);
      });
    });

    const form = fields[0].closest('form');
    if (form) {
      form.addEventListener('submit', function () {
        fields.forEach(removeFormat);
      });
    }
  });
})();
