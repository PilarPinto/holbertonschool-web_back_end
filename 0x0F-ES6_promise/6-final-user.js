import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName);
  let photo = null;
  try {
    photo = await uploadPhoto(fileName);
  } catch (e) {
    photo = `${e.name}: ${e.message}`;
  }
  const obj1 = { status: 'fulfilled', value: user };
  const obj2 = { status: 'rejected', value: photo };
  return [obj1, obj2];
}
