export function getTokenFromLocalStorage() {
    return localStorage.getItem('jwtToken');
}

export function setTokenFromLocalStorage(token, expires) {
  localStorage.setItem('jwtExpires', expires);
  return localStorage.setItem('jwtToken', token);
}
