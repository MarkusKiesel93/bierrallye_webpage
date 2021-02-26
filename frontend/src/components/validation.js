import { extend } from 'vee-validate'
import { required, email } from 'vee-validate/dist/rules'

extend('required', {
  ...required,
  message: '{_field_} ist erforderlich!',
})

extend('email', {
  ...email,
  message: 'Gültige E-Mail Adresse angeben!',
})

extend('checked', {
  validate: value => {
    return value
  },
  message: '{_field_} muss akzeptiert werden!',
})

extend('hash', {
  validate: value => {
    let upperLettersDigits = true
    return value.length === 6 && upperLettersDigits
  },
  message: 'Stornocode besteht genau aus 6 Zeichen (Ziffern und Buchstaben)!',
})
