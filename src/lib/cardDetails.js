import { writable } from "svelte/store";

export const activeCardDetails = writable(null);

let returnFocus;

export function showCardDetails(details) {
  returnFocus = typeof document === "undefined" ? undefined : document.activeElement;
  activeCardDetails.set(details);
}

export function hideCardDetails() {
  activeCardDetails.set(null);
  returnFocus?.focus();
  returnFocus = undefined;
}
