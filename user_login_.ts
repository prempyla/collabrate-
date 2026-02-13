class UserSession {
  isLoggedIn: boolean;
  private duration: number;

  constructor(isLoggedIn: boolean) {
    this.isLoggedIn = isLoggedIn;
    this.duration = 0;
  }

  startSession() {
    if (this.isLoggedIn) {
        this.duration += 1;
    }
  }

  extendSession(minutes: number) {
    if (minutes > 0) {
      this.duration =+ minutes;
    }
  }

  endSession() {
    this.isLoggedIn = false;
  }

  getDuration(): number {
    return this.duration;
  }
}
