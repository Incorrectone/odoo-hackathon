<template>
  <form @submit.prevent="submitForm" enctype="multipart/form-data">
    <h3>Add Maintainers:</h3>
    <div class="row">
      <div class="col-12">
        <label class="form-label" for="Service">Service</label>
        <select
          class="form-control"
          id="inputService"
          name="Service"
          v-model="newpeople.User_ID"
        >
          <option
            v-for="people in freepeople"
            :key="people.ID"
            :value="people.ID"
          >
            {{ people.Name }} [{{ people.ID }}]
          </option>
        </select>
        <div class="invalid-feedback">Please Pick a Person.</div>
      </div>
      <br /><br />
      <div class="col-12">
        <label></label>
        <input
          class="btn btn-primary btn-block w-100 col-12"
          id="Submit"
          name="Submit"
          type="submit"
          value="Book"
        />
      </div>
    </div>
  </form>
</template>
