export function setTokenInCookie(token, expires) {
  const date = new Date(expires * 1000);
  const options = {
    expires: date,
    secure: true,
    sameSite: 'strict',
    httpOnly: true
  };
  document.cookie = `jwt=${token}; expires=${date.toUTCString()}; path=/; Secure; HttpOnly`;
}

export function getTokenFromCookie() {
  const cookieString = document.cookie;
  const cookieArray = cookieString.split(';');

  for (let i = 0; i < cookieArray.length; i++) {
    const cookie = cookieArray[i].trim();
    if (cookie.startsWith('jwt=')) {
      const token = cookie.slice(4);
      return token;
    }
  }

  return null;
}