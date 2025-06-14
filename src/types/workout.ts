interface Exercise {
  name: string;
  sets: number;
  reps: number;
  weight?: number;
}

interface Workout {
  id: string;
  name: string;
  time: number;
  exercises: Array<Exercise>
}

export type {Workout, Exercise}
